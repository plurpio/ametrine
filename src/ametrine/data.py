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
                themes.append(themePath)
                logging.info("Found Valid Theme: "+i)
            except: logging.warning("Invalid theme: "+i, exc_info=None)
        else: logging.warning("Invalid theme: "+i, exc_info=None)
    return themes
