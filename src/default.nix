with import <nixpkgs> {};
with pkgs.python3Packages;

buildPythonPackage rec {
  name = "ametrine";
  author="Plurpio";
  description="A CLI application to switch configuration files on the fly!";
  src = ./.;
  doCheck = false;
  propagatedBuildInputs = [ python311Packages.click python311Packages.pyyaml python311Packages.setuptools ];
}

