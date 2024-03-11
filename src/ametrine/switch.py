import os
import logging
import themes
import settings

def changeTheme(theme):
    if theme not in themes.getThemes():
        logging.error("invalid theme: "+theme)
        return "invalid theme"

    if themes.themeConfig(theme, "precmds"):
        for i in themes.themeConfig(theme, "precmds"):
            logging.info("Running precmd for theme "+theme+": "+i)
            os.system(i)

    if settings.setting("precmds") and themes.themeConfig(theme, "usemainprecmds"):
        for i in settings.setting("precmds"):
            logging.info("Running precmd: "+i)
            os.system(i)

    for (root,dirs,files) in os.walk(themes.themePath(theme), topdown=True):
        for i in files:
            symlinkPath = os.path.join(root.replace(themes.themePath(theme), os.path.expanduser("~"))+"/"+i)
            if symlinkPath == os.path.join(os.path.expanduser("~"), "config.yaml"):
                logging.info("skipping config.yaml with path: "+root+"/"+i)
                continue
            if os.path.exists(os.path.dirname(symlinkPath)) == False:
                os.makedirs(os.path.dirname(symlinkPath))
                logging.info("creating dir: "+os.path.dirname(symlinkPath))
            try:
                if os.path.islink(symlinkPath) == True:
                    os.remove(symlinkPath)
                    logging.warning("overwriting symlink for path "+symlinkPath)
                logging.info("symlinking "+os.path.join(root, i)+" to "+symlinkPath)
                os.symlink(os.path.join(root, i), symlinkPath)
            except:
                if settings.setting("overwritefiles"):
                    os.remove(symlinkPath)
                    os.symlink(os.path.join(root, i), symlinkPath)
                    logging.warning("overwrited "+symlinkPath+" with symlink")
                else:
                    logging.error("real file at location "+symlinkPath+" enable overwritefiles in config.yaml or delete file in that location.")


    if themes.themeConfig(theme, "aftercmds"):
        for i in themes.themeConfig(theme, "aftercmds"):
            logging.info("Running aftercmd for theme "+theme+": "+i)
            os.system(i)

    if settings.setting("aftercmds") and themes.themeConfig(theme, "usemainaftercmds"):
        for i in settings.setting("aftercmds"):
            logging.info("Running aftercmd: "+i)
            os.system(i)
