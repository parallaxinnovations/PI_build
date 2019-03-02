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

install_reqs = parse_requirements("requirements.txt", session=PipSession())
reqs = [str(ir.req) for ir in install_reqs]

# add a few more requirements
if sys.platform == 'win32':
    reqs.extend(['pefile'])

setup(name='PI_build',
      version=version,
      license="Commercial",
      description="Parallax Innovations Build scripts",
      author="Jeremy D. Gill",
      author_email="jgill@parallax-innovations.com",
      maintainer="Jeremy D. Gill",
      maintainer_email="jgill@parallax-innovations.com",
      requires=reqs,
      tests_require=['pytest', 'tempdir>=0.7.1', 'future'],
      install_requires=reqs,
      url="http://www.parallax-innovations.com",
      packages=['PI_build'],
      long_description="Parallax Innovations Build scripts",
)
