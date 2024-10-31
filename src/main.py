"""
Team 63344Z
Season 2024-2025.
"""

import sys
from vex import *
import urandom

brain = Brain()


# region config
controller = Controller(PRIMARY)  # Primary controller
motor_left_front = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)  # Left front motor
motor_right_front = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)  # Right front motor
motor_left_back = Motor(Ports.PORT9, GearSetting.RATIO_18_1, True)  # Left back motor
motor_right_back = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)  # Right back motor
intake = Motor(Ports.PORT8, GearSetting.RATIO_18_1, True)  # intake motor
sender = Motor(Ports.PORT7, GearSetting.RATIO_18_1, True)  # sender motor
p = DigitalOut(brain.three_wire_port.a)  # Pneumatic motor


# gyro
# jumpA = DigitalIn(brain.three_wire_port.a)

# motor groups
mgl = MotorGroup(motor_left_front, motor_left_back)
mgr = MotorGroup(motor_right_front, motor_right_back)
# integrated motor groups
# smartDrive = SmartDrive(mgl, mgr, Gyro, 319.19, 3600, 3000, MM, 1.4) # no gyro sensor
# end of region config

# start of initialization
global FULL_SPEED
FULL_SPEED = 100
# end of initialization

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
    """
    intake_control: done
    drivetrain_control: done
    pneumatic_control: done
    sender_control: TBD
    climb_control: TBD
    """
    while True:
        intake_control()
        drivetrain_control()
        pneumatic_control()
        sender_control()
        climb_control()
        
        # wait for the driver control period to end
        wait(20, MSEC)

        if controller.buttonLeft.pressing():
            pass
            
        # Pneumatic control
        valve_open = False
        # L2 button: 
        if controller.buttonL2.pressing(): 
            ###if not valve_open:
                # p1.open()
                # valve_open = True
                # wait(1000, MSEC)
            # else:
                # p1.close()
                # valve_open = False
                # wait(1000, MSEC)
            pass
        
        if controller.buttonL1.pressing():
            pass
                
        if controller.buttonUp.pressing():
            pass

        if controller.buttonDown.pressing():
            pass
        else:
            pass
    
def intake_control():
    """ intake control
    R1 button: switch intake direction
    R2 button: switch intake on/off
    """
    if controller.buttonR1.pressing():  # R1 button: intake backward
        intake.spin(FORWARD, FULL_SPEED, PERCENT)
    elif controller.buttonR2.pressing():  # R2 button: intake forward
        intake.spin(REVERSE, FULL_SPEED, PERCENT)
    else:
        intake.stop(COAST)
    
def drivetrain_control():
        # Controller Axis 1 and Axis 3:
        # The left front motor and left back motor spin FORWARD when pushing the left joystick FORWARD.
        # Then, the left front motor and left back motor spin backward when pushing the left joystick backward.
        motor_left_front.spin(FORWARD, controller.axis1.value() + controller.axis3.value(), PERCENT)
        motor_left_back.spin(FORWARD, controller.axis1.value() + controller.axis3.value(), PERCENT)
        motor_right_front.spin(FORWARD, controller.axis1.value() - controller.axis3.value(), PERCENT)
        motor_right_back.spin(FORWARD, controller.axis1.value() - controller.axis3.value(), PERCENT)

def pneumatic_control():
    p.set(False)
    if controller.buttonL1.pressing():
        p.set(True)
    elif controller.buttonL2.pressing():
        p.set(False)

def sender_control():
    pass
def climb_control():
    pass

# allows access to Competition methods
competition = Competition(driver_control, autonomous)