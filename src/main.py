"""
Team 63344Z
Robot Yaju
Season 2024-2025.
"""

import sys
from vex import *
import urandom

brain = Brain()


# region config
controller = Controller(PRIMARY)  # primary controller
motor_left_front = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)  # left front motor
motor_right_front = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)  # right front motor
motor_left_mid = Motor(Ports.PORT2, GearSetting.RATIO_36_1, True)  # left middle motor
motor_right_mid = Motor(Ports.PORT9, GearSetting.RATIO_18_1, True)  # right middle motor
motor_left_back = Motor(Ports.PORT3, GearSetting.RATIO_36_1, True)  # left back motor
motor_right_back = Motor(Ports.PORT8, GearSetting.RATIO_18_1, True)  # right back motor
sender = Motor(Ports.PORT20, GearSetting.RATIO_18_1, True)  # sender motor
p = DigitalOut(brain.three_wire_port.b)  # pneumatic motor
# gyro
# jumpA = DigitalIn(brain.three_wire_port.a)

# motor groups
mgl = MotorGroup(motor_left_front, motor_left_mid, motor_left_back)
mgr = MotorGroup(motor_right_front, motor_right_mid, motor_right_back)

# drivetrain
drivetrain = DriveTrain(mgl, mgr, 319.19, 3600, 3000, MM, 1.4)
# end of region config

# Constants
FULL_SPEED = 100

# Global variables
valve_open = False

def initialize_autonomous():
    """
    Initialize the autonomous control tasks.
    """
    _autonomous_thread = Thread(autonomous)

    while (competition.is_autonomous() and competition.is_enabled()):
        wait(10, MSEC)
        
    _autonomous_thread.stop()

def initialize_driver_control():
    """
    Initialize the driver control tasks.
    """
    _driver_thread = Thread(driver_control)

    while (competition.is_driver_control() and competition.is_enabled()):
        wait(10, MSEC)

    # stop the driver control tasks
    _driver_thread.stop()

def autonomous():
    """
    Autonomous control function.
    """
    mgl.spin(FORWARD, 50, PERCENT)
    mgr.spin(REVERSE, 50, PERCENT)
    wait(0.5, SECONDS)
    mgl.stop(COAST)
    mgr.stop(COAST)
    
    
    
def driver_control():
    """
    Driver control function.
    """
    while True:
        drivetrain_control()
        pneumatic_control()
        sender_control()
        climb_control() # TODO
        
        wait(10, MSEC)
        
def sender_control():
    """
    Control the sender motor based on controller input. The sender motor controls the intake.
    """
    if controller.buttonR1.pressing():  # R1 button: intake backward
        sender.spin(FORWARD, FULL_SPEED, PERCENT)
    elif controller.buttonR2.pressing():  # R2 button: intake forward
        sender.spin(REVERSE, FULL_SPEED, PERCENT)
    else:
        sender.stop(COAST)

        
def drivetrain_control():
    """
    Control the drivetrain motors based on controller input.
    """
    forward_speed = controller.axis3.value()
    turn_speed = controller.axis1.value()
    
    drivetrain.drive(FORWARD, forward_speed, PERCENT)
    drivetrain.turn(RIGHT, turn_speed, PERCENT)
    
    # motor_left_front.spin(REVERSE, controller.axis1.value() + controller.axis3.value(), PERCENT)
    # motor_left_back.spin(REVERSE, controller.axis1.value() + controller.axis3.value(), PERCENT)
    # motor_left_mid.spin(REVERSE, controller.axis1.value() + controller.axis3.value(), PERCENT)
    # motor_right_front.spin(REVERSE, controller.axis1.value() - controller.axis3.value(), PERCENT)
    # motor_right_back.spin(REVERSE, controller.axis1.value() - controller.axis3.value(), PERCENT)
    # motor_right_mid.spin(REVERSE, controller.axis1.value() - controller.axis3.value(), PERCENT)
    
def pneumatic_control():
    """
    Control the pneumatic valve based on controller input.
    """
    global valve_open
    
    if controller.buttonL1.pressing():
        valve_open = True
    elif controller.buttonL2.pressing():
        valve_open = False
        
    p.set(valve_open)
        
def climb_control():
    """
    Control the climbing mechanism.
    """
    #TODO: implement climbing mechanism control
    pass

# allows access to Competition methods
competition = Competition(driver_control, autonomous)
