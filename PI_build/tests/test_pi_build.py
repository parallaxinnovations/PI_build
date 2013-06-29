import os
from .. import build_tools

def test_basic():
    """Package import and basic usage"""

    _dir = os.path.join(os.path.dirname(__file__), '..', '..')
    info = build_tools.get_version_strings(_dir)
    assert(isinstance(info.VER_PRODUCT_MAJOR, str))
    assert(isinstance(info.VER_PRODUCT_MINOR, str))
    assert(isinstance(info.VER_PRODUCT_REVISION, str))
    assert(isinstance(info.VER_PRODUCT_BUILD, str))
    assert(isinstance(info.SHORT_SHA1, str))
    assert(isinstance(info.FULL_VERSION, str))
    assert(isinstance(info.VERSION, str))
    assert(isinstance(info.SHORT_VERSION, str))
    assert(isinstance(info.MAINTAINER, str))
    assert(isinstance(info.MAINTAINER_EMAIL, str))
    assert(info.MAINTAINER == 'Jeremy Gill')