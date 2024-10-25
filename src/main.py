"""
Ensure all hardware components are properly connected and configured before running the program.
This program is for the competition match.

Team 63344Z
Season 2024-2025.
"""

import sys
from vex import *
import urandom
# from config import *
# from autonomous import autonomous
# from driver_control import driver_control

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
intake = Motor(Ports.PORT8, GearSetting.RATIO_18_1, False)  # intake motor
p1 = Pneumatics(DigitalOut(brain.three_wire_port.a))  # Pneumatic motor


# sensor
# jumpA = DigitalIn(brain.three_wire_port.a)

# motor groups
mgl = MotorGroup(motor_left_front, motor_left_back)
mgr = MotorGroup(motor_right_front, motor_right_back)
# integrated motor groups
smartDrive = SmartDrive(mgl, mgr, 0,0) # no gyro sensor
""" sample code
    smartDrive = SmartDrive(mgl, mgr, )
    drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 319.19, 295, 40, MM, 1)
    
    wheel size = 4 inches
    track width = 295mm
    wheelbase = 40mm
    gear ratio = 1(input):1(output)
    gear cartridge = 18:1
"""
# end of region config

FULL_SPEED = 100

# wait for rotation sensor to fully initialize
wait(30, MSEC)

# pneumatic valve initialization
p1.close()

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

def autonomous():
    # TBD
    pass

def driver_control():
    intake.spin(FORWARD, FULL_SPEED, PERCENT)
    # place drive control code here, inside the loop
    while True:
        # This is the main loop for the driver control.
        # Each time through the loop you should update motor
        # movements based on input from the controller.
        
        # Controller Axis 1 and Axis 3:
        # The left front motor and left back motor spin FORWARD when pushing the left joystick FORWARD.
        # Then, the left front motor and left back motor spin backward when pushing the left joystick backward.
        motor_left_front.spin(REVERSE, controller.axis1.value() + controller.axis3.value(), PERCENT)
        motor_left_back.spin(REVERSE, controller.axis1.value() + controller.axis3.value(), PERCENT)
        motor_right_front.spin(REVERSE, controller.axis1.value() - controller.axis3.value(), PERCENT)
        motor_right_back.spin(REVERSE, controller.axis1.value() - controller.axis3.value(), PERCENT)

        # R1 and R2 buttons:
        # The right arm motor and left arm motor lift up the arms at once when pressing the R1 button.
        # Then, the right arm motor and left arm motor lift down the arms at once when pressing the R2 button.
        if controller.buttonLeft.pressing():
            pass
            
        # Pneumatic control
        valve_open = False
        # L2 button: 
        if controller.buttonL2.pressing(): 
            if not valve_open:
                p1.open()
                valve_open = True
                wait(1000, MSEC)
            else:
                p1.close()
                valve_open = False
                wait(1000, MSEC)

        if controller.buttonL1.pressing():
            pass
        
        # intake control
        # R1 button: switch intake direction
        intake_spin_direction = True # forward
        if controller.buttonR1.pressing():
            intake.spin(REVERSE, FULL_SPEED, PERCENT)
            intake_spin_direction = False
            wait(30, MSEC)
        else:
            intake.spin(FORWARD, FULL_SPEED, PERCENT)
            intake_spin_direction = True
            wait(30, MSEC)

        # R2 button: switch intake on/off
        intake_spin_state = True
        if controller.buttonR2.pressing():
            intake.spin(FORWARD, FULL_SPEED, PERCENT)

        if controller.buttonUp.pressing():
            pass

        if controller.buttonDown.pressing():
            pass
        else:
            pass
            
# allows access to Competition methods
competition = Competition(driver_control, autonomous)