import StarLAB
import time

rover = StarLAB.Connect(IP="192.168.1.2")
rover.enableRover()

global running  # flag tracking if a state is currently running

# Tunables
approach_time = 12  # time to drive to chair in s
approach_velocity = 100  # percentage speed forwards
drive_straight_difference = 3  # subtracted from the right motor

pivot_velocity = 100  # percentage pivot speed
pivot_time = 31  # pivot time in s
pivot_motor_delta = 20  # subtracted from left motor to turn

return_time = 13  # time to return from chair in s
return_velocity = approach_velocity  # percentage speed forwards

def drive(motor_value: int, duration: float) -> None:
    """
    Run the motors in the same direction to drive forwards.
    Param: motor_value - a posative or negative percentage to drive both motors at.
    Param: duration - time in seconds to drive for.
    """

    if motor_value > 100 or motor_value < -100:
        # confirm the values are within bounds
        raise ValueError

    running = True
    start_time = time.monotonic()
    current_time = start_time
    # timer setup

    while current_time < (start_time + duration):
        current_time = time.monotonic()
        rover.motors.setMotorPower(motor_value - drive_straight_difference, motor_value)
    rover.motors.setMotorPower(0, 0)


def pivot(motor_value: int, motor_delta: int, duration: float) -> None:
    """Pivot around the chair, a posative delta is a counter-clockwise or left turn."""
    if motor_value > 100 or motor_value < -100:
        # confirm the values are within bounds
        raise ValueError

    running = True
    left_motor_value = motor_value
    right_motor_value = motor_value
    if motor_delta > 0:
        # deterimne which way we are turning
        left_motor_value -= motor_delta
    elif motor_delta < 0:
        right_motor_value -= motor_delta

    start_time = time.monotonic()
    current_time = start_time
    # timer setup


    while current_time < (start_time + duration):
        current_time = time.monotonic()
        rover.motors.setMotorPower(100, 70)
    rover.motors.setMotorPower(0, 0)


start_time = time.monotonic()
drive(approach_velocity, approach_time)
pivot(pivot_velocity, pivot_motor_delta, pivot_time)
drive(return_velocity, return_time)
print(f"This test took {time.monotonic()-start_time} seconds to complete.")
