{ pkgs ? import <nixpkgs> {}, packages ? pkgs.python3Packages }:

packages.buildPythonPackage rec {
  pname = "PI_build";
  version = "0.1.4";

  src = ./.;
  format = "pyproject";

  nativeBuildInputs = [
    packages.hatchling
    packages.hatch-vcs
  ];

  propagatedBuildInputs = [
    packages.dulwich
    packages.psutil
  ];

  checkInputs = [
    packages.pytestCheckHook
    packages.pytest-cov
    packages.pytest-asyncio
  ];

  doCheck = true;

  meta = with pkgs.lib; {
    description = "Parallax Innovations Build scripts";
    homepage = "https://parallaxinnovations.github.io/PI_build/";
    license = licenses.bsd3;
    maintainers = [ "Jeremy Gill <jgill@parallax-innovations.com>" ];
  };
}
