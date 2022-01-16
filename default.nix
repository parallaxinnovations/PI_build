{ pkgs, buildPythonPackage, packages }:
buildPythonPackage rec {
  pname = "PI_build";
  version = "0.1.3-55";

  src = fetchGit {
    url = "ssh://git@bitbucket.org/jgill72/PI_build.git";
    rev = "86c7cf49a956d093223654493791a99ba4eb2e6f";
    allRefs = true;
  };

  preBuild = ''
    export PACKAGE_VERSION="0.1.3"
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
