import sys
sys.path.append('../')
import time
from Common_Libraries.p0_lib import *

import os
from Common_Libraries.repeating_timer_lib import repeating_timer

def update_sim ():
    try:
        my_qbot.ping()
    except Exception as error_update_sim:
        print (error_update_sim)


speed = 0.1 # in m/s
my_qbot = qbot(speed)
update_thread = repeating_timer(2, update_sim)

#---------------------------------------------------------------------------------
# STUDENT CODE BEGINS
#---------------------------------------------------------------------------------

start_time = time.time()
my_qbot.forward (5.58)
my_qbot.rotate(-90)
my_qbot.forward (7.12)
my_qbot.rotate(-105)
my_qbot.forward (11.16)
my_qbot.rotate(-90)
my_qbot.forward (7.12)
my_qbot.rotate(-100)
my_qbot.forward (5.58)
end_time = time.time()
print (end_time - start_time)
