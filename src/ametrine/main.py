#
# Imports
#

import sys
import logging
import os
import click

#
# Configure pretty logging
#

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', datefmt='%H:%M:%S', level=logging.INFO)
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', datefmt='%H:%M:%S', level=logging.WARNING)
logging.basicConfig(format='%(asctime)s %(levelname)s %(module)s -> %(funcName)s: %(message)s', datefmt='%H:%M:%S', level=logging.ERROR)
logging.basicConfig(format='%(asctime)s %(levelname)s %(module)s -> %(funcName)s: %(message)s', datefmt='%H:%M:%S', level=logging.CRITICAL)

if os.getenv("DEBUG") or len(sys.argv) >= 2 and sys.argv[1] == "debug":
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug("Logging enabled.")
else:
    logging.getLogger().setLevel(logging.CRITICAL)


#
# Main App
#

if __name__ == "__main__":
    print("bob")
else:
    import data
    import switch
    import themes
    import settings
