let
  pkgs = import <nixpkgs> {};
in
  pkgs.mkShell {
    buildInputs = [
      (pkgs.callPackage ./default.nix { pkgs=pkgs; })
      pkgs.python3Packages.pycairo
      pkgs.python3Packages.cairosvg
      pkgs.python3Packages.mkdocs
      pkgs.python3Packages.mkdocs-material
      pkgs.python3Packages.mkdocs-material-extensions
      pkgs.python3Packages.pymdown-extensions
    ];
    # create a virtual environment and install python packages
    # that aren't yet available from nixpkgs, e.g. fontawesome-markdown
    shellHook = ''
      python -m venv --system-site-packages .venv
      source .venv/bin/activate
      pip install -r docs/requirements.txt
      echo
      echo "Development environment for MkDocs with Material theme is ready."
      echo "You can run 'mkdocs serve' to start the local server."
      echo "To build the documentation, run 'mkdocs build'."
      echo "To deploy the documentation, run 'mkdocs gh-deploy'."
      echo "To install additional Python packages, use 'pip install <package-name>'."
      echo "To exit the shell, type 'exit'."
      '';
  }
