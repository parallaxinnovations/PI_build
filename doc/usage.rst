Usage
=====

An example :file:`setup.py` file is listed below for demonstration purposes::

	from distutils.core import setup
	from PI_build import build_tools

        # get the directory where our :file:``setup.py`` is
        _dir = os.path.dirname(__file__)

        # get version info for this project
	info = build_tools.get_version_strings(_dir)

	# We'll use the contents of PI_build to put version strings in __init__.py
	f = open(os.path.join('PI','recon','__init__.py'), 'wt')
	f.write('PACKAGE_SHA1="%s"\n' % info.PACKAGE_SHA1)
	f.write('PACKAGE_VERSION="%s"\n' % info.VERSION)
	f.close()

	# Here we use the library to create appropriate Windows resource files	
	for filename in glob.glob(os.path.join('Windows', '*.rc.in')):
	    s = open(filename, 'rb').read() % info.get_dictionary()
	    f = open(filename.replace('.in',''), 'wb')
	    f.write(s)
	    f.close()

	setup(
		name = 'MY PROJECT',
		version = info.VERSION,
		packages = mypackage,
	)
