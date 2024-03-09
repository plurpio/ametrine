import data
import os
import logging

def changeTheme(theme):
    if theme not in data.getThemes():
        logging.error("invalid theme: "+theme)
        return "invalid theme"
