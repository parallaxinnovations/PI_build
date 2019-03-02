.. Parallax Innovations Python build tools documentation master file, created by
   sphinx-quickstart on Thu Jun 20 23:37:08 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

PI_build Docs
=============
This python package contains tools to automatically maintain version info for python
software packages that are kept in git repositories.  Tag projects with names that look like
`vA.B.C`, and `PI_build` can be used to automatically populate version strings elsewhere.  This package
depends primarily on  `dulwhich <http://http://www.samba.org/~jelmer/dulwich/>`_, which is used to
directly query software repositories.

Contents
========

.. toctree::
   :maxdepth: 2

   install
   usage
   classes

