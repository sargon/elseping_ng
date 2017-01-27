with import <nixpkgs> {}; {
  pyEnv = stdenv.mkDerivation {
    name = "py";
    buildInputs = [ stdenv 
                    python35
                  ];
    LIBRARY_PATH="${libxml2}/lib";
    shellHook = ''
      pip3 install --user django
      pip3 install --user db-sqlite3
      export PATH=$PATH:~/.local/bin
      export PYTHONPATH=$PYTHONPATH:~/.local/lib/python3.5/site-packages
    '';
  };
}
