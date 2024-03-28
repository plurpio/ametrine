<div align = center>

<img src="src/github/banner.png" width="960" height="360" alt="banner">

<br>


<br>
Ametrine is a CLI application to switch configuration files on the fly!
<br>
<br>

</div>

## configuration
To run ametrine use the command `ametrine`
Running that will automatically put configuration files in `$HOME/.config/ametrine/`, configuration files have documentation embedded into the file. <br><br>

Your theme folder defined in `$HOME/.config/ametrine/config.yaml`, it should contain themes that are seperated into folders. Create a theme folder and run `ametrine theme config >>> config.yaml` to make a theme-specific configuration file. All other files that are not `config.yaml` will be symlinked from your home directory when running `ametrine change THEME`.

## cli
`ametrine` main command <br>
`ametrine change` changes your theme <br>

`ametrine cleanup` cleanup traces of your last theme <br>
`ametrine cleanup all` does ametrine cleanup but for every theme <br>
`ametrine cleanup THEME` does ametrine cleanup for a specific theme <br>

`ametrine theme ls` lists all your themes (made to be scriptable) <br>
`ametrine theme config` prints out default theme config <br>

## intergration with other apps
You may want to intergrate ametrine into other apps to make changing themes easier. Here is an example with intergration with tofi. This one-liner will make a tofi selection window with all valid themes and lets you choose one to apply. You can modify this to work with other run launchers such as rofi and dmenu. <br>
`ametrine change $(ametrine theme ls | tofi --prompt "What theme do you want?")`

## installation
Packages aren't avaliable for now so you have to build Ametrine yourself. <br>

1. clone the repo and cd into src<br>
```git clone https://github.com/plurpio/ametrine; cd ametrine/src```

Installation is pretty simple you just have to choose your method.

**The nix way**
Use this if your on NixOS or have the Nix package manager installed.
```nix-env -f default.nix -i```

**The pip way**
Use this for everything else that isn't NixOS
```python -m build; pip install dist/*.whl```

## development
To start developing for ametrine follow these steps:
1. Fork the repo <br>

2. Clone your fork<br>
`git clone https://github.com/YOURUSERNAME/ametrine`

3. CD into the src directory <br>
`cd ametrine/src/ametrine`

4. Create a python virtual enviroment and install dependencies <br>
`python3 -m venv venv; pip install -r requirements.txt`

5. Enable debug logs <br>
`export DEBUG=1`

6. Test compiling with your changes <br>
`cd ..; nix-build # Testing with nix build`

7. Create a pull request<br>
