import os
import sys

sys.path.append(os.path.abspath('../'))

from Services.Clock import Clock
from Utils import Methods

Methods.restore_json_file()

clock_instance = Clock()
clock_instance.clock()


