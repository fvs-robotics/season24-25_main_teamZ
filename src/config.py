"""
Ensure all hardware components are properly connected and configured before running the program.
This program is for the competition match.

Team 63344Z
Season 2024-2025.
Final edit: 9.23.2024.
"""

import vex
from vex import *

brain = Brain()

# region config
controller = Controller(PRIMARY)  # Primary controller
motor_left_front = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)  # Left front motor
motor_right_front = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)  # Right front motor
motor_left_back = Motor(Ports.PORT12, GearSetting.RATIO_18_1, False)  # Left back motor
motor_right_back = Motor(Ports.PORT19, GearSetting.RATIO_18_1, False)  # Right back motor
arm_left = Motor(Ports.PORT11, GearSetting.RATIO_36_1, False)  # Left arm motor
arm_right = Motor(Ports.PORT20, GearSetting.RATIO_36_1, False)  # Right arm motor
intake = Motor(Ports.PORT8, GearSetting.RATIO_18_1, False)  # intake motor
launcher = Motor(Ports.PORT6, GearSetting.RATIO_18_1, False)  # Launcher motor
jumpA = DigitalIn(brain.three_wire_port.a)
pneumatic = Pneumatics(Ports.PORT7)  # Pneumatic motor
# end of region config