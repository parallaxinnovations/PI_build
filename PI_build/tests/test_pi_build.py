import os
from .. import build_tools
import pytest

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
    vals = info.get_dictionary()

def test_fail():
    """Point package at a wrong folder"""

    _dir = os.path.join(os.path.dirname(__file__), '..', '..', '..')

    with pytest.raises(Exception):
        info = build_tools.get_version_strings(_dir)
