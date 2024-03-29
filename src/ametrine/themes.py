import os
import logging
from ametrine import settings
import yaml


def getThemes():
    """list all themes"""
    themes = []
    for i in os.listdir(settings.setting("themepath")):
        themePath = settings.setting("themepath")+"/"+i
        if os.path.isdir(themePath) == True and os.listdir(themePath) != []:
            try:
                open(themePath+"/config.yaml")
                themes.append(i)
            except: logging.warning("Invalid theme: "+i, exc_info=None)
        else: logging.warning("Invalid theme: "+i, exc_info=None)
    return themes


def themeConfig(theme, setting):
    """returns a requested setting from a theme"""
    if theme not in getThemes():
        return "invalid theme"
    themepath = settings.setting("themepath")+"/"+theme
    with open(os.path.join(themepath, "config.yaml")) as file:
        f = yaml.safe_load(file)
        return f[setting]

def themePath(theme):
    """returns the path of a theme"""
    if theme not in getThemes():
        return "invalid theme"
    return os.path.join(settings.setting("themepath"), theme)

def baseIntergrity():
    if settings.setting("basetheme") == "" or settings.setting("basetheme") == "invalid setting" or settings.setting("basetheme") in getThemes(): return []
    """returns if the basetheme is applied correctly currently"""
    notgood = [] # peak programming naming right here
    for (root,dirs,files) in os.walk(themePath(settings.setting("basetheme")), topdown=True):
        for i in files:
            symlinkPath = os.path.join(root.replace(themePath(settings.setting("basetheme")), os.path.expanduser("~"))+"/"+i)
            if os.path.exists(os.path.dirname(symlinkPath)) == False:
                notgood.append(symlinkPath)
    return notgood
