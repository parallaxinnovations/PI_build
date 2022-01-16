{ pkgs, buildPythonPackage, packages }:
buildPythonPackage rec {
  pname = "PI_build";
  version = "0.1.3-51-g24831f9";

  src = fetchGit {
    url = "ssh://git@bitbucket.org/jgill72/PI_build.git";
    rev = "24831f9e84f0d931fe8189088d70f9592a3f29c0";
    allRefs = true;
  };

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
