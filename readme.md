<div align = center>

<img src="src/github/banner.png" width="800" height="300" alt="banner">

<br>


<br>
Ametrine is a CLI application to switch configuration files on the fly!
<br>
<br>

</div>

## configuration
To run ametrine run the command `ametrine`
Running that will automatically put configuration files in `$HOME/.config/ametrine/`, main configuration contains documentation to help you.

Your theme folder defined in `$HOME/.config/ametrine/config.yaml` should contain themes seperated into folders, go into/create a theme folder and run `ametrine theme config >>> config.yaml` to make a theme-specific configuration file. All other files that are not `config.yaml` will be symlinked from your home directory when running `ametrine change THEME`.

## cli
`ametrine` main command <br>
`ametrine change` changes your theme <br>

`ametrine cleanup` cleanup traces of your last theme <br>
`ametrine cleanup all` does ametrine cleanup but for every theme <br>
`ametrine cleanup THEME` does ametrine cleanup for a specific theme <br>

`ametrine theme ls` lists all your themes (made to be scriptable) <br>
`ametrine theme config` prints out default theme config <br>

## intergration with other apps
You may want to intergrate ametrine into other apps to make changing themes easier. Here is an example with intergration with tofi. This snippet of bash will make a tofi window popup with all valid themes and let you choose one to apply. You may need to modify this to work with other run launchers such as rofi and dmenu. <br>
`ametrine change $(ametrine theme ls | tofi --prompt "What theme do you want?")`

## development
To start developing for ametrine follow these steps:
1. Clone the repo <br>
`git clone https://github.com/plurpio/ametrine`

2. CD into the src directory <br>
`cd ametrine/src/ametrine`

3. Create a python virtual enviroment and install dependencies <br>
`python3 -m venv venv; pip install -r requirements.txt`

4. Enable debug logs <br>
`export DEBUG=1`

5. Test compiling with your changes <br>
`cd ..; nix-build # Testing with nix build`
<br>