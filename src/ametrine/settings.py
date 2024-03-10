import yaml
import os
import logging
import shutil

#
# Getting config location
#

if os.getenv("XDG_CONFIG_HOME"):
    settingsPath = os.path.join(os.getenv("XDG_CONFIG_HOME"), "ametrine")
    if os.path.exists(settingsPath) == False: os.makedirs(settingsPath)
    logging.info("Using "+settingsPath+" as config directory")
elif os.getenv("HOME"):
    logging.warning("XDG_CONFIG_HOME is not set!")
    settingsPath = os.getenv("HOME")+"/.config/ametrine"
    if os.path.exists(settingsPath) == False: os.makedirs(settingsPath)
    logging.info("Using "+settingsPath+" as config directory")
else:
    logging.critical("How did we get here? Are you even running linux? $HOME and $XDG_CONFIG_HOME aren't set.")
    quit()

#
# Create config is not exist
#

if not os.path.exists(os.path.join(settingsPath, "config.yaml")):
    configLocation = os.path.join(os.path.dirname(os.path.realpath(__file__)), "defaultFiles", "mainconfig.yaml")
    with open(configLocation) as f:
        shutil.copy2(configLocation, os.path.join(settingsPath, "config.yaml"))
        logging.info("Created new config.yaml at "+os.path.join(settingsPath, "config.yaml"))

#
# Get settings out of config
#

with open(os.path.join(settingsPath, "config.yaml")) as file:
    f = yaml.safe_load(file)
    f["themepath"] = os.path.expanduser(f["themepath"])
    if os.path.isdir(f["themepath"]) == False:
        logging.critical("Theme path doesn't exist or isn't dir: "+str(f["themepath"]))
        quit()
    logging.info("Successfully loaded main config.")

def setting(setting):
    return f[setting]
