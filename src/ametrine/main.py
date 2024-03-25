#
# Imports
#

import switch
import logging
import themes
import click
import os
import data

#
# Configure pretty logging
#

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', datefmt='%H:%M:%S', level=logging.INFO)
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', datefmt='%H:%M:%S', level=logging.WARNING)
logging.basicConfig(format='%(asctime)s %(levelname)s %(module)s -> %(funcName)s: %(message)s', datefmt='%H:%M:%S', level=logging.ERROR)
logging.basicConfig(format='%(asctime)s %(levelname)s %(module)s -> %(funcName)s: %(message)s', datefmt='%H:%M:%S', level=logging.CRITICAL)

if os.getenv("DEBUG"):
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug("Logging enabled.")
else:
    logging.getLogger().setLevel(logging.CRITICAL)


#
# Main App
#

@click.version_option("0a", prog_name="ametrine")
@click.group()
def cli():
    pass

@cli.group()
def theme():
    """commands related to themes"""
    pass

@theme.command()
def ls():
    """list all valid themes"""
    for i in themes.getThemes():
        print(i)

@theme.command("config")
def config():
    """prints out default theme configuration"""
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "defaultFiles", "themeconfig.yaml")) as f: print(f.read())

@cli.command()
@click.argument("theme")
def change(theme):
    """change to a specific theme"""
    switch.changeTheme(theme)

@cli.command()
@click.argument("theme", required=False)
def cleanup(theme):
    """remove all symlinks of a specific theme, use all for general cleanup"""
    if theme in themes.getThemes(): switch.removeTheme(theme)
    elif data.get("lastTheme") != "": switch.removeTheme(data.get("lastTheme"))
    elif theme == "all": 
        for i in themes.getThemes(): switch.removeTheme(i)
    else: click.UsageError


if __name__ == '__main__':
    cli()
