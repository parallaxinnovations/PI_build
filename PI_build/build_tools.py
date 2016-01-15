#####################################
# Parallax Build tools
#####################################

import os
import pprint
import re
import logging
from dulwich.repo import Repo
from dulwich.errors import NotGitRepository

class NoCompatibleTagDefined(Exception):
    """Raised when there are not correctly formatted tags in the git repository.

    At least one tag of the form v0.0.0 should be defined.
    """
    pass


class PIVersionInfo(object):
    """Encapsulates a project's version info.

    Used internally - you shouldn't need to create one directly.

    .. data:: VER_PRODUCT_MAJOR

       The project's major version number

    .. data:: VER_PRODUCT_MINOR

       The project's minor version number


    .. data:: VER_PRODUCT_REVISION

       The project's revision number

    .. data:: VER_PRODUCT_BUILD

       The project's build number

    .. data:: SHORT_SHA1

       A shortened SHA1 digest representation for the software

    .. data:: FULL_VERSION

       The full version string

    .. data:: VERSION

       A shortened version string

    .. data:: MAINTAINER

       Name of the maintainer of the project

    .. data:: MAINTAINER_EMAIL

       E-mail of the maintainer

    .. data:: TAG
    
       Closest tag name
    """

    def __init__(self):
        """Initialize the object with dummy values.

        :rtype : None
        The default values are of limited value."""
        self.VER_PRODUCT_MAJOR = '0'
        self.VER_PRODUCT_MINOR = '0'
        self.VER_PRODUCT_REVISION = '0'
        self.VER_PRODUCT_BUILD = '1'
        self.SHORT_SHA1 = ''
        self.FULL_VERSION = '0.0.0'
        self.VERSION = ''
        self.TAG = ''
        self.SHORT_VERSION = ''
        self.MAINTAINER = "Jeremy Gill"
        self.MAINTAINER_EMAIL = "jgill@parallax-innovations.com"

    def __str__(self):
        return pprint.pformat(vars(self))

    def get_dictionary(self):
        """Returns a dictionary of version info.

        Call this method if you need to perform string replacements.  The contents
        of the dictionary can be used for automatic string replacments, such as in
        the following example::

        "full_version = %(FULL_VERSION)s" % build_tools.PIVersionInfo().get_dictionary()

        :rtype: A dictionary of version strings
        """
        return {
            'VER_PRODUCT_MAJOR': self.VER_PRODUCT_MAJOR,
            'VER_PRODUCT_MINOR': self.VER_PRODUCT_MINOR,
            'VER_PRODUCT_REVISION': self.VER_PRODUCT_REVISION,
            'VER_PRODUCT_BUILD': self.VER_PRODUCT_BUILD,
            'SHORT_SHA1': self.SHORT_SHA1,
            'FULL_VERSION': self.FULL_VERSION,
            'VERSION': self.VERSION,
            'SHORT_VERSION': self.SHORT_VERSION,
            'MAINTAINER': self.MAINTAINER,
            'MAINTAINER_EMAIL': self.MAINTAINER_EMAIL,
            'TAG': self.TAG[self.TAG.find('-')+1:]
        }


def get_version_strings(_dir):
    """
    A global function that returns a :class:`PIVersionInfo` object, encapsulating your project's version info.

    :param _dir: directory of the toplevel folder in your project.  :file:`.git` should be 
                 found immediately below this directory.
    :rtype: A :class:`PIVersionInfo` object.
    """
    info = PIVersionInfo()
    r = None

    while True:
        try:
            r = Repo(_dir)
            break
        except NotGitRepository:
            _dir2 = os.path.abspath(os.path.join(_dir, '..'))
            if _dir != _dir2:
                _dir = _dir2
            else:
                raise Exception("Unable to find git repository")
    info.PACKAGE_SHA1 = r.get_refs()[b'HEAD']

    sha1_to_tag = {}
    for entry in r.get_refs():
        if 'tags' in entry.decode('utf-8'):
            sha1 = r.get_refs()[entry]
            sha1_to_tag[sha1] = entry.decode('utf-8').replace('refs/tags/', '')

    count = 0
    ex = re.compile('v[0-9]*\.[0-9]*\.[0-9]*$')
    git_version = 'v1.0.0-g0000'

    for walker in r.get_walker():
        commit = walker.commit
        if commit.id in sha1_to_tag:
            # first match is closest tag
            if info.TAG == '':
                info.TAG = sha1_to_tag[commit.id]
            # verify that tag conforms to our needs
            if ex.match(sha1_to_tag[commit.id]):
                git_version = '%s-%d-g%s' % (sha1_to_tag[commit.id], count, r.head()[0:7])
                break
        count += 1

    try:
        info.VER_PRODUCT_MAJOR, info.VER_PRODUCT_MINOR, info.VER_PRODUCT_REVISION, info.VER_PRODUCT_BUILD, info.SHORT_SHA1 = re.compile(
            'v([0-9]*).([0-9]*).([0-9]*)-([0-9]*)-(.*)').match(git_version).groups()
        info.FULL_VERSION = git_version
        info.VERSION = '%s.%s.%s-%s' % (info.VER_PRODUCT_MAJOR, info.VER_PRODUCT_MINOR, info.VER_PRODUCT_REVISION,
                                        info.VER_PRODUCT_BUILD)
        info.SHORT_VERSION = '%s.%s.%s' % (info.VER_PRODUCT_MAJOR, info.VER_PRODUCT_MINOR, info.VER_PRODUCT_REVISION)
    except:
        msg = "No compatible tag defined"
        logging.warning(msg)
        raise NoCompatibleTagDefined(msg)

    return info
