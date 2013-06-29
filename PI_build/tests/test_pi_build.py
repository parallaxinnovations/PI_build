import os
from .. import build_tools
import pytest
import py
from dulwich.repo import Repo

def test_basic():
    """Package import and basic usage"""

    _dir = os.path.join(os.path.dirname(__file__), '..', '..')
    info = build_tools.get_version_strings(_dir)

    # evaluate various types
    assert (isinstance(info.VER_PRODUCT_MAJOR, str))
    assert (isinstance(info.VER_PRODUCT_MINOR, str))
    assert (isinstance(info.VER_PRODUCT_REVISION, str))
    assert (isinstance(info.VER_PRODUCT_BUILD, str))
    assert (isinstance(info.SHORT_SHA1, str))
    assert (isinstance(info.FULL_VERSION, str))
    assert (isinstance(info.VERSION, str))
    assert (isinstance(info.SHORT_VERSION, str))
    assert (isinstance(info.MAINTAINER, str))
    assert (isinstance(info.MAINTAINER_EMAIL, str))
    assert (info.MAINTAINER == 'Jeremy Gill')

    # make sure we can get the dictionary
    info.get_dictionary()

def test_fail():
    """Point package at a wrong folder"""

    _dir = os.path.join(os.path.dirname(__file__), '..', '..', '..')

    with pytest.raises(Exception):
        build_tools.get_version_strings(_dir)

def test_missing_label(tmpdir):
    """Test git repository with incorrect label"""

    # create a temp directory
    _dir = str(tmpdir.mkdir("repo"))

    # initialize a git repo here
    Repo.init(_dir)

    # test for failure
    with pytest.raises(KeyError):
        info = build_tools.get_version_strings(_dir)
