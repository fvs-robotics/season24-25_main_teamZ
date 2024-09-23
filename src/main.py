"""
Ensure all hardware components are properly connected and configured before running the program.
This program is for the competition match.

Season 2024-2025.
Final edit: 9.23.2024.
"""

import sys
import vex
from vex import *
import urandom

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


# end of region config

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


def autonomous():
    # Segment 1

    arm_left.spin(FORWARD, 100, PERCENT)
    arm_right.spin(REVERSE, 100, PERCENT)
    wait(0.3, SECONDS)

    arm_left.spin(REVERSE, 100, PERCENT)
    arm_right.spin(FORWARD, 100, PERCENT)
    wait(0.3, SECONDS)

    intake.spin(FORWARD, 100, PERCENT)
    wait(0.2, SECONDS)

    motor_left_front.spin(REVERSE, 100, PERCENT)
    motor_left_back.spin(REVERSE, 100, PERCENT)
    motor_right_front.spin(FORWARD, 100, PERCENT)
    motor_right_back.spin(FORWARD, 100, PERCENT)
    wait(0.3,SECONDS)

    motor_left_front.stop(HOLD)
    motor_right_front.stop(HOLD)
    motor_left_back.stop(HOLD)
    motor_right_back.stop(HOLD)
    wait(0.05, SECONDS)

    # Segment 2

    motor_left_front.spin(REVERSE, 80, PERCENT)
    motor_left_back.spin(REVERSE, 80, PERCENT)
    motor_right_front.spin(REVERSE, 80, PERCENT)
    motor_right_back.spin(REVERSE, 80, PERCENT)
    wait(0.2, SECONDS)

    motor_left_front.spin(REVERSE, 100, PERCENT)
    motor_left_back.spin(REVERSE, 100, PERCENT)
    motor_right_front.spin(FORWARD, 100, PERCENT)
    motor_right_back.spin(FORWARD, 100, PERCENT)
    wait(0.48, SECONDS)

    motor_left_front.spin(FORWARD, 100, PERCENT)
    motor_left_back.spin(FORWARD, 100, PERCENT)
    motor_right_front.spin(FORWARD, 100, PERCENT)
    motor_right_back.spin(FORWARD, 100, PERCENT)
    wait(0.33, SECONDS)

    motor_left_front.stop(HOLD)
    motor_right_front.stop(HOLD)
    motor_left_back.stop(HOLD)
    motor_right_back.stop(HOLD)
    wait(0.01,SECONDS)

    arm_left.spin(FORWARD, 100, PERCENT)
    arm_right.spin(REVERSE, 100, PERCENT)
    wait(0.3, SECONDS)

    motor_left_front.spin(REVERSE, 100, PERCENT)
    motor_left_back.spin(REVERSE, 100, PERCENT)
    motor_right_front.spin(FORWARD, 100, PERCENT)
    motor_right_back.spin(FORWARD, 100, PERCENT)
    wait(0.52, SECONDS)

    motor_left_front.stop(HOLD)
    motor_right_front.stop(HOLD)
    motor_left_back.stop(HOLD)
    motor_right_back.stop(HOLD)
    wait(0.01,SECONDS)


    # Segment 3

    motor_left_front.spin(REVERSE, 100, PERCENT)
    motor_left_back.spin(REVERSE, 100, PERCENT)
    motor_right_front.spin(FORWARD, 100, PERCENT)
    motor_right_back.spin(FORWARD, 100, PERCENT)
    wait(0.52,SECONDS)

    motor_left_front.spin(FORWARD, 70, PERCENT)
    motor_left_back.spin(FORWARD, 70, PERCENT)
    motor_right_front.spin(REVERSE, 70, PERCENT)
    motor_right_back.spin(REVERSE, 70, PERCENT)
    wait(0.27,SECONDS)

    arm_left.spin(REVERSE, 100, PERCENT)
    arm_right.spin(FORWARD, 100, PERCENT)
    wait(0.6,SECONDS)

    motor_left_front.stop(BRAKE)
    motor_right_front.stop(BRAKE)
    motor_left_back.stop(BRAKE)
    motor_right_back.stop(BRAKE)
    wait(0.1, SECONDS)


    # Segment 4

    motor_left_front.spin(FORWARD, 80, PERCENT)
    motor_left_back.spin(FORWARD, 80, PERCENT)
    motor_right_front.spin(FORWARD, 80, PERCENT)
    motor_right_back.spin(FORWARD, 80, PERCENT)
    wait(0.34,SECONDS)

    motor_left_front.spin(REVERSE, 100, PERCENT)
    motor_left_back.spin(REVERSE, 100, PERCENT)
    motor_right_front.spin(FORWARD, 100, PERCENT)
    motor_right_back.spin(FORWARD, 100, PERCENT)
    wait(0.1,SECONDS)

    intake.spin(FORWARD, 100, PERCENT)
    wait(0.3,SECONDS)

    motor_left_front.spin(REVERSE, 70, PERCENT)
    motor_left_back.spin(REVERSE, 70, PERCENT)
    motor_right_front.spin(REVERSE, 70, PERCENT)
    motor_right_back.spin(REVERSE, 70, PERCENT)
    wait(0.07,SECONDS)

    motor_left_front.spin(REVERSE, 100, PERCENT)
    motor_left_back.spin(REVERSE, 100, PERCENT)
    motor_right_front.spin(FORWARD, 100, PERCENT)
    motor_right_back.spin(FORWARD, 100, PERCENT)
    wait(0.9,SECONDS)

    motor_left_front.stop(HOLD)
    motor_right_front.stop(HOLD)
    motor_left_back.stop(HOLD)
    motor_right_back.stop(HOLD)
    wait(0.01,SECONDS)


    # Segment 5

    motor_left_front.spin(REVERSE, 100, PERCENT)
    motor_left_back.spin(REVERSE, 100, PERCENT)
    motor_right_front.spin(REVERSE, 100, PERCENT)
    motor_right_back.spin(REVERSE, 100, PERCENT)
    wait(0.488, SECONDS)

    motor_left_front.spin(REVERSE, 90, PERCENT)
    motor_left_back.spin(REVERSE, 90, PERCENT)
    motor_right_front.spin(FORWARD, 90, PERCENT)
    motor_right_back.spin(FORWARD, 90, PERCENT)
    wait(0.1,SECONDS)

    arm_left.spin(FORWARD, 85, PERCENT)
    arm_right.spin(REVERSE, 85, PERCENT)
    wait(0.4, SECONDS)

    motor_left_front.spin(REVERSE, 100, PERCENT)
    motor_left_back.spin(REVERSE, 100, PERCENT)
    motor_right_front.spin(FORWARD, 100, PERCENT)
    motor_right_back.spin(FORWARD, 100, PERCENT)
    wait(0.8,SECONDS)

    motor_left_front.stop(BRAKE)
    motor_right_front.stop(BRAKE)
    motor_left_back.stop(BRAKE)
    motor_right_back.stop(BRAKE)
    wait(0.01,SECONDS)

    # Segment 6 

    motor_left_front.stop(HOLD)
    motor_right_front.stop(HOLD)
    motor_left_back.stop(HOLD)
    motor_right_back.stop(HOLD)
    arm_left.stop(HOLD)
    arm_right.stop(HOLD)

    motor_left_front.spin(FORWARD, 80, PERCENT)
    motor_left_back.spin(FORWARD, 80, PERCENT)
    motor_right_front.spin(FORWARD, 80, PERCENT)
    motor_right_back.spin(FORWARD, 80, PERCENT)
    wait(0.3, SECONDS)

    arm_left.spin(REVERSE, 85, PERCENT)
    arm_right.spin(FORWARD, 85, PERCENT)
    wait(0.4, SECONDS)



    motor_left_front.stop(HOLD)
    motor_right_front.stop(HOLD)
    motor_left_back.stop(HOLD)
    motor_right_back.stop(HOLD)
    arm_left.stop(HOLD)
    arm_right.stop(HOLD)
    wait(0.01,SECONDS)

def initialize_driver_control():
    # start the driver control tasks
    _driver_thread = Thread(driver_control)

    # wait for the driver control period to end
    while (competition.is_driver_control() and competition.is_enabled()):
        # wait 10 milliseconds before checking again
        wait(10, MSEC)

    # stop the driver control tasks
    _driver_thread.stop()


def driver_control():
    intake.spin(FORWARD, FULL_SPEED, PERCENT)
    # place drive control code here, inside the loop
    while True:
        # This is the main loop for the driver control.
        # Each time through the loop you should update motor
        # movements based on input from the controller.

        # (for debugging only) Temperature return:
        # Every movement will return the temperature of the motor on the brain screen.
        # tempArmL = arm_left.temperature()
        # tempArmR = arm_right.temperature()
        # brain.screen.clear_screen()
        # brain.screen.print(tempArmL)
        # brain.screen.print(tempArmR)

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
            launcher.spin(FORWARD, FULL_SPEED, PERCENT)
            wait(0.9, SECONDS)
            launcher.stop(HOLD)
            
        if controller.buttonL1.pressing():
            arm_left.spin_for(REVERSE, FULL_SPEED, PERCENT)
            arm_right.spin_for(FORWARD, FULL_SPEED, PERCENT)
            wait(0.3, SECONDS)

        elif controller.buttonL2.pressing():
            arm_left.spin_for(FORWARD, FULL_SPEED, PERCENT)
            arm_right.spin_for(REVERSE, FULL_SPEED, PERCENT)
            wait(0.3, SECONDS)

        elif controller.buttonR1.pressing():
            intake.spin(REVERSE, FULL_SPEED, PERCENT)

        elif controller.buttonR2.pressing():
            intake.spin(FORWARD, FULL_SPEED, PERCENT)

        if controller.buttonUp.pressing():
            launcher.spin(FORWARD, FULL_SPEED, PERCENT)

        if controller.buttonDown.pressing():
            launcher.set_position(0, DEGREES)
            launcher.stop(HOLD)

        else:
            # Stop the arms only if neither ButtonL2 nor ButtonL1 is pressed
            arm_left.stop(HOLD)
            arm_right.stop(HOLD)

            wait(20, MSEC)
# allows access to Competition methods
competition = Competition(driver_control, autonomous)