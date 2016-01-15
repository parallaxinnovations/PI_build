# =========================================================================
# Copyright (c) 2011-2016 Parallax Innovations Inc.
# =========================================================================

import os
from distutils.core import setup

# do it using git here to avoid depending on dulwich at this point
version = os.popen('git describe --tags').read().strip().replace('v','')

setup(name='PI_build',
      version=version,
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
