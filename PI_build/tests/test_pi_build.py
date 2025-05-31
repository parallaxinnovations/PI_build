import os
from PI_build import build_tools
import pytest
from tempfile import TemporaryDirectory
from dulwich.repo import Repo, Tag

def test_basic():
    """Package import and basic usage"""

    _dir = os.path.join(os.path.dirname(__file__), '..', '..')
    info = build_tools.get_version_strings(_dir)

    # evaluate various types
    assert isinstance(info.VER_PRODUCT_MAJOR, str)
    assert isinstance(info.VER_PRODUCT_MINOR, str)
    assert isinstance(info.VER_PRODUCT_REVISION, str)
    assert isinstance(info.VER_PRODUCT_BUILD, str)
    assert isinstance(info.SHORT_SHA1, str)
    assert isinstance(info.FULL_VERSION, str)
    assert isinstance(info.VERSION, str)
    assert isinstance(info.SHORT_VERSION, str)
    assert isinstance(info.MAINTAINER, str)
    assert isinstance(info.MAINTAINER_EMAIL, str)
    assert info.MAINTAINER == 'Jeremy Gill'

    # make sure we can get the dictionary
    info.get_dictionary()


def test_missing_label():
    """Test git repository with incorrect label"""

    with TemporaryDirectory() as _dir:

        # initialize a git repo here
        repo = Repo.init(_dir)

        # put in some content
        repo.do_commit(b'test commit', committer=b'anonymous <anonymous@anonymous.com>')

        # test for failure
        with pytest.raises(build_tools.NoCompatibleTagDefined):
            build_tools.get_version_strings(_dir)


def test_correct_label():
    """Test git repository with a correct label"""

    with TemporaryDirectory() as _dir:

        # initialize a git repo here
        repo = Repo.init(_dir)

        # put in some content
        repo.do_commit(b'test commit', committer=b'anonymous <anonymous@anonymous.com>')
        commit = repo.get_object(repo.head())

        # tag it
        tag = Tag()
        tag.tagger = b'anonymous <anonymous@anonymous.com>'
        tag.message = b'version 1.2.3 released'
        tag.name = b'v1.2.3'
        tag.object = (commit, commit.id)
        tag.tag_time = commit.author_time
        tag._tag_timezone = 0
        repo.object_store.add_object(tag)
        repo[b'refs/tags/' + tag.name] = commit.id

        info = build_tools.get_version_strings(_dir)
        assert info.SHORT_VERSION == '1.2.3'