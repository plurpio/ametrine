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

    if themes.themeConfig(theme, "aftercmds"):
        for i in themes.themeConfig(theme, "aftercmds"):
            logging.info("Running aftercmd for theme "+theme+": "+i)
            os.system(i)

    if settings.setting("aftercmds") and themes.themeConfig(theme, "usemainaftercmds"):
        for i in settings.setting("aftercmds"):
            logging.info("Running aftercmd: "+i)
            os.system(i)
