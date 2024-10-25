import sys
import vex
from vex import *
import urandom
from config import *

FULL_SPEED = 100

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
        if controller.buttonL2.pressing(): 
            p1.open() # down button pneumatic valve extends
            valve_open = True
        elif controller.buttonL1.pressing(): 
            p1.close() # up button pneumatic valve retracts
            valve_open = False
        elif valve_open:
            p1.open() # valve keeps open
        else:
            p1.close() # valve closes
            
        # intake control
        if controller.buttonR1.pressing():
            intake.spin(REVERSE, FULL_SPEED, PERCENT)

        if controller.buttonR2.pressing():
            intake.spin(FORWARD, FULL_SPEED, PERCENT)

        if controller.buttonUp.pressing():
            pass

        if controller.buttonDown.pressing():
            pass
        else:
            # Stop the arms only if neither ButtonL2 nor ButtonL1 is pressed
            arm_left.stop(HOLD)
            arm_right.stop(HOLD)

            wait(20, MSEC)