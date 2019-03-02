import os
from .. import build_tools
import pytest
from tempdir import TempDir
from dulwich.repo import Repo, Tag

def test_basic():
    """Package import and basic usage"""

    _dir = os.path.join(os.path.dirname(__file__), '..', '..')
    info = build_tools.get_version_strings(_dir)

    # evaluate various types
    assert (isinstance(info.VER_PRODUCT_MAJOR, basestring))
    assert (isinstance(info.VER_PRODUCT_MINOR, basestring))
    assert (isinstance(info.VER_PRODUCT_REVISION, basestring))
    assert (isinstance(info.VER_PRODUCT_BUILD, basestring))
    assert (isinstance(info.SHORT_SHA1, basestring))
    assert (isinstance(info.FULL_VERSION, basestring))
    assert (isinstance(info.VERSION, basestring))
    assert (isinstance(info.SHORT_VERSION, basestring))
    assert (isinstance(info.MAINTAINER, basestring))
    assert (isinstance(info.MAINTAINER_EMAIL, basestring))
    assert (info.MAINTAINER == 'Jeremy Gill')

    # make sure we can get the dictionary
    info.get_dictionary()


#def test_fail():
#    """Point package at a wrong folder"""
#
#    _dir = os.path.join(os.path.dirname(__file__), '..', '..', '..')
#    with pytest.raises(Exception):
#        build_tools.get_version_strings(_dir)


def test_missing_label():
    """Test git repository with incorrect label"""

    with TempDir() as _dir:

        # initialize a git repo here
        repo = Repo.init(_dir)

        # put in some content
        repo.do_commit('test commit', committer='anonymous <anonymous@anonymous.com>')

        # test for failure
        with pytest.raises(build_tools.NoCompatibleTagDefined):
            info = build_tools.get_version_strings(_dir)


def test_correct_label():
    """Test git repository with a correct label"""

    with TempDir() as _dir:

        # initialize a git repo here
        repo = Repo.init(_dir)

        # put in some content
        repo.do_commit('test commit', committer='anonymous <anonymous@anonymous.com>')
        commit = repo.get_object(repo.head())

        # tag it
        tag = Tag()
        tag.tagger = 'anonymous <anonymous@anonymous.com>'
        tag.message = 'version 1.2.3 released'
        tag.name = 'v1.2.3'
        tag.object = (commit, commit.id)
        tag.tag_time = commit.author_time
        tag._tag_timezone = 0
        repo.object_store.add_object(tag)
        repo['refs/tags/' + tag.name] = commit.id

        info = build_tools.get_version_strings(_dir)
        assert(info.SHORT_VERSION == '1.2.3')