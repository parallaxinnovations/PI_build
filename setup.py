# =========================================================================
# Copyright (c) 2011-2019 Parallax Innovations Inc.
# =========================================================================

import os
import sys
from setuptools import setup

try:
    from pip._internal.req.req_file import parse_requirements
    from pip._internal.download import PipSession
except:
    from pip.req import parse_requirements
    from pip.download import PipSession

# do it using git here to avoid depending on dulwich at this point
version = os.popen('git describe --tags').read().strip().replace('v','')

reqs = [
    'dulwich',
    'psutil'
]

if sys.platform == 'win32':
    reqs.append('pefile')


setup(name='PI_build',
      version=version,
      license="BSD License",
      description="Parallax Innovations Build scripts",
      author="Jeremy D. Gill",
      author_email="jgill@parallax-innovations.com",
      maintainer="Jeremy D. Gill",
      maintainer_email="jgill@parallax-innovations.com",
      setup_requires=['pytest-runner'],
      requires=reqs,
      tests_require=['pytest', 'pytest-cov', 'tempdir>=0.7.1', 'future', 'codecov'],
      install_requires=reqs,
      url="http://www.parallax-innovations.com",
      packages=['PI_build'],
      long_description="Parallax Innovations Build scripts",
)
