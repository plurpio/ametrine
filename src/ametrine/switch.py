import os
import logging
from ametrine import themes
from ametrine import settings
from ametrine import data

def removeTheme(theme):
    for (root,dirs,files) in os.walk(themes.themePath(data.get("lastTheme")), topdown=True):
        for i in files:
            symlinkPath = os.path.join(root.replace(themes.themePath(theme), os.path.expanduser("~"))+"/"+i)
            if os.path.islink(symlinkPath) == True:
                os.remove(symlinkPath)
                logging.info("removing old theme symlink: "+symlinkPath)
            elif os.path.exists(symlinkPath) == False: pass
            else: logging.warning("file is at expected symlink location! "+symlinkPath)


def changeTheme(theme):
    """switch to the theme requested"""
    # check if theme valid
    if theme not in themes.getThemes():
        logging.error("invalid theme: "+theme)
        return "invalid theme"


    # run theme-specific precmds
    if themes.themeConfig(theme, "precmds"):
        for i in themes.themeConfig(theme, "precmds"):
            logging.info("Running precmd for theme "+theme+": "+i)
            os.system(i)

    # runs main config precmds
    if settings.setting("precmds") and themes.themeConfig(theme, "usemainprecmds"):
        for i in settings.setting("precmds"):
            logging.info("Running precmd: "+i)
            os.system(i)

    # removes last theme
    if data.get("lastTheme") and data.get("lastTheme") != settings.setting("basetheme"):
        removeTheme(data.get("lastTheme"))

    # checks base theme integrity
    if settings.setting("basetheme") != "":
        for i in themes.baseIntergrity():
            symlinkPath = i.replace(themes.themePath(settings.setting("basetheme")), os.path.expanduser("~"))
            if os.path.exists(os.path.dirname(symlinkPath)) == False: os.makedirs(os.path.dirname(symlinkPath))
            if symlinkPath == os.path.join(os.path.expanduser("~"), "config.yaml"): continue
            if os.path.exists(symlinkPath) == True and os.path.islink(symlinkPath) == False:
                logging.error("real file at location "+symlinkPath+" enable overwritefiles in config.yaml or delete file in that location.")
                continue
            elif os.path.islink(symlinkPath) == True: os.remove(symlinkPath)
            os.symlink(i, symlinkPath)
            logging.info("symlinked base "+i+" to "+symlinkPath)

    # symlinks theme files
    if not settings.setting("basetheme") == theme:
        for (root,dirs,files) in os.walk(themes.themePath(theme), topdown=True):
            for i in files:
                symlinkPath = os.path.join(root.replace(themes.themePath(theme), os.path.expanduser("~")), i)
                if symlinkPath == os.path.join(os.path.expanduser("~"), "config.yaml"):
                    logging.info("skipping config.yaml with path: "+root+"/"+i)
                    continue
                if os.path.exists(os.path.dirname(symlinkPath)) == False:
                    os.makedirs(os.path.dirname(symlinkPath))
                    logging.info("creating dir: "+os.path.dirname(symlinkPath))
                try:
                    if os.path.islink(symlinkPath) == True:
                        os.remove(symlinkPath)
                    logging.info("symlinking "+os.path.join(root, i)+" to "+symlinkPath)
                    os.symlink(os.path.join(root, i), symlinkPath)
                except:
                    if settings.setting("overwritefiles"):
                        os.remove(symlinkPath)
                        os.symlink(os.path.join(root, i), symlinkPath)
                        logging.warning("overwrited "+symlinkPath+" with symlink")
                    else:
                        logging.error("real file at location "+symlinkPath+" enable overwritefiles in config.yaml or delete file in that location.")


    # runs theme-specific aftercmds
    if themes.themeConfig(theme, "aftercmds"):
        for i in themes.themeConfig(theme, "aftercmds"):
            logging.info("Running aftercmd for theme "+theme+": "+i)
            os.system(i)

    # runs main config aftercmds
    if settings.setting("aftercmds") and themes.themeConfig(theme, "usemainaftercmds"):
        for i in settings.setting("aftercmds"):
            logging.info("Running aftercmd: "+i)
            os.system(i)

    # sets lastTheme to new theme
    data.setValue("lastTheme", theme)
