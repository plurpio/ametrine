import rich
import os
import logging

path = str(os.getenv("HOME"))+"/repos/ametrine/src/ametrine/themes"
if os.path.exists(path) == False: os.makedirs(path)

def getThemes():
    themes = []
    for i in os.listdir(path):
        themePath = path+"/"+i
        if os.listdir(path+"/"+i) != []:
            try:
                open(themePath+"/config.toml")
                themes.append(themePath)
                logging.info("Found Valid Theme: "+i)
            except: logging.warning("Invalid theme: "+i, exc_info=None)
        else: logging.warning("Invalid theme: "+i, exc_info=None)
    return themes
