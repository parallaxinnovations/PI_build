let
  pkgs = import <nixpkgs> {};
in
  pkgs.mkShell {
    buildInputs = [
      (pkgs.callPackage ./default.nix { pkgs=pkgs; })
    ];
  }
