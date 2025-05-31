# PI_build Docs

Parallax Innovations python build tools.

[PI_build](index.md) contains tools to automatically maintain version info for python
software packages that are kept in git repositories.  This project predominantly exists to aid
in packaging [MicroView](http://microview.parallax-innovations.com) but may be useful for other purposes as well.
Modern python packages should consider using things like [hatch-vcs](https://github.com/ofek/hatch-vcs) or [setuptools-scm](https://setuptools-scm.readthedocs.io/en/latest/) instead.

Tag projects with names that look like
`vA.B.C`, and *PI_build* can be used to automatically populate version strings elsewhere.  This package
depends primarily on  [dulwhich](https://www.dulwich.io/), which is used to directly query software repositories.

## Quick Links

* [Changelog](changelog.md)
* [Installation](install.md)
* [Usage](usage.md)
