import json
import os
import logging

#
# Getting data location
#

if os.getenv("XDG_CONFIG_HOME") and os.getenv("XDG_CONFIG_HOME") != None:
    dataPath = os.path.join(os.getenv("XDG_CONFIG_HOME"), "ametrine", "data.json")
    if os.path.exists(os.path.dirname(dataPath)) == False: os.makedirs(os.path.dirname(dataPath))
    logging.info("using "+dataPath+" as data file")
elif os.getenv("HOME") and os.getenv("HOME") != None:
    logging.warning("XDG_CONFIG_HOME is not set!")
    dataPath = os.path.join(os.getenv("HOME"), "ametrine", "data.json")
    if os.path.exists(os.path.dirname(dataPath)) == False: os.makedirs(os.path.dirname(dataPath))
    logging.info("using "+dataPath+" as data file")
else:
    logging.critical("How did we get here? Are you even running linux? $HOME and $XDG_CONFIG_HOME aren't set.")
    quit()

#
# get data out of file
#

if not os.path.exists(dataPath):
    with open(dataPath, "w+", encoding='utf-8') as f:
        data = {}
        json.dump(data, f)
        data = json.dumps(data)
        data = json.loads(data)
        logging.warning("data file doesn't exist, creating one")
else:
    with open(dataPath) as file:
        try:
            data = json.load(file)
        except:
            logging.error("invalid data for datafile")
            logging.debug("data file contains:\n"+file.read())
            os.remove(dataPath)
            with open(dataPath, "w+", encoding='utf-8') as f:
                data = {}
                json.dump(data, f)
                data = json.dumps(data)
                data = json.loads(data)
logging.info("successfully loaded main config.")

#
# library part
#

def get(setting):
    if setting not in data:
        logging.error("invalid value requested: "+setting)
        return "invalid setting"
    return data[setting]

def setValue(value, thing):
    data[value] = thing
    with open(dataPath, "w", encoding='utf-8') as f:
        json.dump(data, f)
    return "success"
