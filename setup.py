# =========================================================================
# Copyright (c) 2011-2019 Parallax Innovations Inc.
# =========================================================================

import os
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

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



class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


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
      cmdclass = {'test': PyTest},
      packages=['PI_build'],
      long_description="Parallax Innovations Build scripts",
)
