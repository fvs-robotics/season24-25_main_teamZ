"""
Ensure all hardware components are properly connected and configured before running the program.

Team 63344Z
Season 2024-2025.
"""

import vex
from vex import *

brain = Brain()


# region config
### 
# TODO:
# 1. Correct ports for motors and sensors after the robot is built.
# 2. Correct the gear ratio for the motors.
# 3. a sensor is undecided: figure out the correct ports and types.
# 4. Jumper: figure out how to make the switch work.
###

controller = Controller(PRIMARY)  # Primary controller
motor_left_front = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)  # Left front motor
motor_right_front = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)  # Right front motor
motor_left_back = Motor(Ports.PORT9, GearSetting.RATIO_18_1, True)  # Left back motor
motor_right_back = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)  # Right back motor
intake = Motor(Ports.PORT8, GearSetting.RATIO_18_1, True)  # intake motor
p1 = Pneumatics(Ports.PORT7)  # Pneumatic motor


# sensor
# jumpA = DigitalIn(brain.three_wire_port.a)

# motor groups
mgl = MotorGroup(motor_left_front, motor_left_back)
mgr = MotorGroup(motor_right_front, motor_right_back)
# integrated motor groups
# smartDrive = SmartDrive(mgl, mgr) # a sensor is needed

# end of region config