# =========================================================================
# Copyright (c) 2011-2014 Parallax Innovations Inc.
# =========================================================================

import os
from distutils.core import setup
from PI_build import build_tools

_dir = os.path.dirname(__file__)
info = build_tools.get_version_strings(_dir)

setup(name='PI_build',
      version=info.SHORT_VERSION,
      license="Commercial",
      description="Parallax Innovations Build scripts",
      author="Jeremy D. Gill",
      author_email="jgill@parallax-innovations.com",
      maintainer="Jeremy D. Gill",
      maintainer_email="jgill@parallax-innovations.com",
      requires=['dulwich'],
      url="http://www.parallax-innovations.com",
      packages=['PI_build'],
      long_description="Parallax Innovations Build scripts",
)
