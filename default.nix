{ pkgs, buildPythonPackage, packages }:
buildPythonPackage rec {
  pname = "PI_build";
  version = "0.1.4";

  src = fetchGit {
    url = "ssh://git@bitbucket.org/jgill72/PI_build.git";
    rev = "362c3057c4b2fde4dee4dc939dac4f575f0b7e0a";
    allRefs = true;
  };

  preBuild = ''
    echo '__version__ = "${version}"' > PI_build/__init__.py
    export PACKAGE_VERSION="${version}"
  '';

  nativeBuildInputs = [
    packages.pip
    pkgs.git
    packages.dulwich
    packages.psutil
  ];

  doCheck = false;

  buildInputs = [
    packages.dulwich
    packages.pip
    packages.psutil
    packages.setuptools
    pkgs.git
  ];

  propagatedBuildInputs = [
    packages.dulwich
    packages.psutil
  ];

  meta = with pkgs.lib; {
    description = "Parallax Innovations Build scripts";
    homepage = "http://www.parallax-innovations.com";
    license = licenses.bsd3;
    maintainers = [ "Jeremy Gill <jgill@parallax-innovations.com>" ];
  };
}
