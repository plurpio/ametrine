#
# Imports
#

import sys
import logging

#
# Configure pretty logging
#

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', datefmt='%H:%M:%S', level=logging.INFO)
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', datefmt='%H:%M:%S', level=logging.WARNING)
logging.basicConfig(format='%(asctime)s %(levelname)s %(module)s -> %(funcName)s: %(message)s', datefmt='%H:%M:%S', level=logging.ERROR)
logging.basicConfig(format='%(asctime)s %(levelname)s %(module)s -> %(funcName)s: %(message)s', datefmt='%H:%M:%S', level=logging.CRITICAL)

logging.disable(logging.CRITICAL)
if len(sys.argv) >= 2 and sys.argv[1] == "debug":
    logging.disable(logging.NOTSET)
    logging.info("Logging enabled.")

#
# Main App
#

