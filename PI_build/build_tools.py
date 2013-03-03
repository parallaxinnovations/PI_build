#####################################
# Parallax Build tools
#####################################

import os
import re
from dulwich.repo import Repo

class PIVersionInfo(object):

    def __init__(self):
    
        self.VER_PRODUCT_MAJOR    = '0'
        self.VER_PRODUCT_MINOR    = '0'
        self.VER_PRODUCT_REVISION = '0'
        self.VER_PRODUCT_BUILD    = '1'
        self.SHORT_SHA1           = ''
        self.FULL_VERSION         = ''
        self.VERSION              = ''
        self.MAINTAINER           = "Jeremy Gill"
        self.MAINTAINER_EMAIL = "jgill@parallax-innovations.com"

def get_version_strings(_dir):

    '''
    Returns a variety of git-related version strings
    '''
    info = PIVersionInfo()

    while True:
        try:
            r = Repo(_dir)
            break
        except:
            _dir2 = os.path.abspath(os.path.join(_dir, '..'))
            if _dir != _dir2:
                _dir = _dir2
            else:
                raise "Unable to find git repository"

    info.PACKAGE_SHA1 = r.get_refs()['HEAD']

    sha1_to_tag = {}
    for entry in r.get_refs():
        if 'tags' in entry:
            sha1 = r.get_refs()[entry]
            sha1_to_tag[sha1] = entry.replace('refs/tags/','')

    count = 0
    ex = re.compile('v[0-9]*\.[0-9]*\.[0-9]*$')

    for walker in r.get_walker():
        commit = walker.commit
        if commit.id in sha1_to_tag:
            # verify that tag conforms to our needs
            if ex.match(sha1_to_tag[commit.id]):
                git_version = '%s-%d-g%s' % (sha1_to_tag[commit.id], count, r.head()[0:7])
                break
        count += 1

    info.VER_PRODUCT_MAJOR, info.VER_PRODUCT_MINOR, info.VER_PRODUCT_REVISION, info.VER_PRODUCT_BUILD, info.SHORT_SHA1 = re.compile('v([0-9]*).([0-9]*).([0-9]*)-([0-9]*)-(.*)').match(git_version).groups()
    info.FULL_VERSION = git_version
    info.VERSION = '%s.%s.%s-%s' % (info.VER_PRODUCT_MAJOR, info.VER_PRODUCT_MINOR, info.VER_PRODUCT_REVISION, info.VER_PRODUCT_BUILD)
    
    return info
