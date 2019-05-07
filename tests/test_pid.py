from hypothesis import given
from hypothesis.strategies import floats
import random

from pid import PID


def read():
    return 1


pid = PID(read)


@given(
    kp=floats(allow_infinity=False, allow_nan=False),
    ki=floats(allow_infinity=False, allow_nan=False),
    kd=floats(allow_infinity=False, allow_nan=False),
    kf=floats(allow_infinity=False, allow_nan=False),
    setpoint=floats(allow_infinity=False, allow_nan=False),
    minimum=floats(allow_infinity=False, allow_nan=False),
    maximum=floats(allow_infinity=False, allow_nan=False),
)
def test_pid(kp, ki, kd, kf, setpoint, minimum, maximum):
    pid.set_gains(kp, ki, kd, kf)
    pid.set_setpoint(setpoint)
    try:
        pid.set_range(minimum, maximum)
    except ValueError as err:
        if err.args[0] == "minimum bound must be less than maximum bound":
            return
        else:
            raise
    try:
        output = pid.get()
    except OverflowError as err:
        if err.args[0] == "error_i has overflowed, please tune your PID":
            return
        else:
            raise
    # print(output)
    assert output >= minimum and output <= minimum
