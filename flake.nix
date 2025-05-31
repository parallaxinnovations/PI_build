{
  description = "Parallax Innovations Build scripts (Python, Hatchling, Nix flake)";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.05";

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
    in {
      packages.${system}.default = import ./default.nix { pkgs = pkgs; };

      devShells.${system}.default = pkgs.mkShell {
        buildInputs = [
          pkgs.python3
          pkgs.python3Packages.hatchling
          pkgs.python3Packages.hatch-vcs
          pkgs.python3Packages.dulwich
          pkgs.python3Packages.psutil
          pkgs.python3Packages.pytest
          pkgs.python3Packages.pytest-cov
          pkgs.python3Packages.pytest-asyncio
        ];
      };
    };
}