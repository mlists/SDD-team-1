import StarLAB
import time

rover = StarLAB.Connect(IP="****.****.****.****")  # TODO update this
rover.enableRover()


def spin(motor_value: int, duration: float) -> None:
    """\
    Run the motors in opposite directions to turn on the spot.
    Param: motor_value - a posative or negative percentage.
    Param: duration - time in seconds to turn for.
    """
    if motor_value > 100 or motor_value < -100:
        # confirm the values are within bounds
        raise ValueError
    start_time = time.monotonic()
    current_time = start_time
    while current_time < (start_time + duration):
        current_time = time.monotonic()
        rover.motors.setMotorPower(motor_value, -motor_value)
    else:
        rover.motors.setMotorPower(0, 0)
        # next state goes here
        pass


spin(50, 3)
