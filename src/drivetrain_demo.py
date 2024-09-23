"""
Ensure all hardware components are properly connected and configured before running the program.
This program is for the competition match.

Season 2024-2025.
Final edit: 9.23.2024.
"""
# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

# Robot configuration code
left_drive_smart = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right_drive_smart = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 319.19, 295, 40, MM, 1)

# Begin project code
drivetrain.drive(FORWARD)

# Print all Drivetrain sensing values to the screen in an infinite loop
while True:
    # Clear the screen and set the cursor to top left corner on each loop
    brain.screen.clear_screen()
    brain.screen.set_cursor(1,1)

    brain.screen.print("Velocity:", drivetrain.velocity(PERCENT))
    brain.screen.next_row()

    brain.screen.print("Current:", drivetrain.current(CurrentUnits.AMP))
    brain.screen.next_row()

    brain.screen.print("Power:", drivetrain.power(PowerUnits.WATT))
    brain.screen.next_row()

    brain.screen.print("Torque:", drivetrain.torque(TorqueUnits.NM))
    brain.screen.next_row()

    brain.screen.print("Efficiency:", drivetrain.efficiency(PERCENT))
    brain.screen.next_row()

    brain.screen.print("Temperature:", drivetrain.temperature(PERCENT))
    brain.screen.next_row()

    # A brief delay to allow text to be printed without distortion or tearing
    wait(100,MSEC)
    
