from keras import __version__ as kv
kv=int(kv[0])
import platform
pv=int(platform.python_version()[0])
import numpy as np
import scipy.io as sio
from keras.callbacks import Callback
import time
import matplotlib  
matplotlib.use('Agg') # 
import matplotlib.pyplot as plt
from math import ceil

if pv>2:
    import _thread as th
else:
    import thread as th
import os
from os import system
import re
import traceback
import platform
from requests.exceptions import ConnectionError
from fbchat import Client
from fbchat.models import *
