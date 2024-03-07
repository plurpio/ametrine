import data
import os

def changeTheme(theme):
    if theme not in data.getThemes(): return "invalid theme"
