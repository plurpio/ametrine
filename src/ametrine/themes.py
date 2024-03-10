import os
import logging
import settings
import yaml


def getThemes():
    themes = []
    for i in os.listdir(settings.setting("themepath")):
        themePath = settings.setting("themepath")+"/"+i
        if os.listdir(themePath) != []:
            try:
                open(themePath+"/config.yaml")
                themes.append(i)
            except: logging.warning("Invalid theme: "+i, exc_info=None)
        else: logging.warning("Invalid theme: "+i, exc_info=None)
    return themes


def themeConfig(theme, setting):
    if theme not in getThemes():
        return "invalid theme"
    themepath = settings.setting("themepath")+"/"+theme
    with open(os.path.join(themepath, "config.yaml")) as file:
        f = yaml.safe_load(file)
        return f[setting]