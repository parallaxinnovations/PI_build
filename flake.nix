{
  description = "Parallax Innovations Build scripts (Python, Hatchling, Nix flake)";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.05";

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
    in {
      packages.${system}.default = import ./default.nix { pkgs = pkgs; };

      # Define the development shell environment
      # This will include Python, Hatchling, and other necessary packages
      # for development and testing of the project
      devShells.${system} = {
        default = pkgs.mkShell {
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

        # Define a development shell for MkDocs with Material theme
        docs = pkgs.mkShell {
          buildInputs = [
            pkgs.python3Packages.pycairo
            pkgs.python3Packages.cairosvg
            pkgs.python3Packages.mkdocs
            pkgs.python3Packages.mkdocs-material
            pkgs.python3Packages.mkdocs-material-extensions
            pkgs.python3Packages.pymdown-extensions
          ];
          shellHook = ''
            python -m venv --system-site-packages .venv
            source .venv/bin/activate
            pip install -r docs/requirements.txt
            echo "Development environment for MkDocs with Material theme is ready."
            echo "You can run 'mkdocs serve' to start the local server."
            echo "To build the documentation, run 'mkdocs build'."
            echo "To deploy the documentation, run 'mkdocs gh-deploy'."
            echo "To install additional Python packages, use 'pip install <package-name>'."
          '';
        };
      };
    };
}