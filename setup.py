# =========================================================================
# Copyright (c) 2011-2013 Parallax Innovations Inc.
# =========================================================================

import sys, os

from distutils.core import setup

setup(name                  = 'PI_build',
      version               = '0.0.1',
      license               = "Commercial",
      description           = "Parallax Innovations Build scripts",
      author                = "Jeremy D. Gill",
      author_email          = "jgill@parallax-innovations.com",
      maintainer            = "Jeremy D. Gill",
      maintainer_email      = "jgill@parallax-innovations.com",
      requires              = ['dulwich'],
      url                   = "http://www.parallax-innovations.com",
      packages              = ['PI_Build'],
      long_description      = "Parallax Innovations Build scripts",
     )