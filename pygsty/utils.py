import logging

from functools import *

flatten = lambda lst: reduce(lambda l, i: l + flatten(i) if isinstance(i, (list, tuple)) else l + [i], lst, [])

# Set up a logger by default use DEBUG level
# and let applications configure it down.
#
# It will
logger = logging.getLogger("pygsty.application")
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
