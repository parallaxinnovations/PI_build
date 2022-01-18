#{ pkgs ? import <nixpkgs> {} # here we import the nixpkgs package set   
#}:
let
  pkgs = import(fetchTarball "http://nixos.org/channels/nixos-21.05/nixexprs.tar.xz") {};
  my-python-package = ps: ps.callPackage ./default.nix { pkgs=pkgs; buildPythonPackage=pkgs.python39Packages.buildPythonPackage; packages=pkgs.python39Packages; };
  python-with-my-packages = pkgs.python39.withPackages (ps: with ps; [
    (my-python-package ps) 
  ]);
in
python-with-my-packages.env
