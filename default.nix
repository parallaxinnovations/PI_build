{ pkgs ? import <nixpkgs> {} }:
with pkgs.python3Packages;
buildPythonPackage rec {
  pname = "PI_build";
  version = "0.1.4";

  src = ./. ;

  preBuild = ''
    echo '__version__ = "${version}"' > PI_build/__init__.py
    export PACKAGE_VERSION="${version}"
  '';

  nativeBuildInputs = [
    pip
    pkgs.git
    dulwich
    psutil
  ];

  doCheck = false;

  buildInputs = [
    dulwich
    pip
    psutil
    setuptools
    pkgs.git
  ];

  propagatedBuildInputs = [
    dulwich
    psutil
  ];

  meta = with pkgs.lib; {
    description = "Parallax Innovations Build scripts";
    homepage = "http://www.parallax-innovations.com";
    license = licenses.bsd3;
    maintainers = [ "Jeremy Gill <jgill@parallax-innovations.com>" ];
  };
}
