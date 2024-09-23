"""
Ensure all hardware components are properly connected and configured before running the program.
This program is for the competition match.

Team 63344Z
Season 2024-2025.
"""

import sys
from vex import *
import urandom
from config import *
from autonomous import autonomous
from driver_control import driver_control

FULL_SPEED = 100

def initialize_autonomous():
    # start the autonomous control tasks
    _autonomous_thread = Thread(autonomous)
    # wait for the driver control period to end
    while (competition.is_autonomous() and competition.is_enabled()):
        # wait 10 milliseconds before checking again
        wait(10, MSEC)
    # stop the autonomous control tasks
    _autonomous_thread.stop()

def initialize_driver_control():
    # start the driver control tasks
    _driver_thread = Thread(driver_control)

    # wait for the driver control period to end
    while (competition.is_driver_control() and competition.is_enabled()):
        # wait 10 milliseconds before checking again
        wait(10, MSEC)

    # stop the driver control tasks
    _driver_thread.stop()
    
# allows access to Competition methods
competition = Competition(driver_control, autonomous)