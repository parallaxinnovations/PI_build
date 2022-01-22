{ pkgs, packages }:
with packages;
buildPythonPackage rec {
  pname = "PI_build";
  version = "0.1.4";

#  src = ./. ;

  src = fetchGit {
    url = "ssh://git@bitbucket.org/jgill72/PI_build.git";
    rev = "24c52c13afcf992df13e02cdb4d1b5c40bf33589";
    allRefs = true;
  };

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
