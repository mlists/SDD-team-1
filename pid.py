import math
import time


class PID:
    def __init__(self, current: object):
        # a function that returns the current value
        self.current = current
        # initialsie gains
        self.kp = 0
        self.ki = 0
        self.kd = 0
        self.kf = 0
        self.setpoint = 0

        self.maximum = 1
        self.minimum = -1

        self.error_i = 0
        self.last_error = 0
        self.last_time = time.monotonic()

    def set_gains(self, kp: float, ki: float, kd: float, kf: float) -> None:
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.kf = kf

    def set_setpoint(self, setpoint: float) -> None:
        self.setpoint = setpoint
        # print(setpoint)

    def set_range(self, minimum: float, maximum: float) -> None:
        if minimum < maximum:
            self.maximum = maximum
            self.minimum = minimum
        else:
            raise ValueError("minimum bound must be less than maximum bound")

    def get(self):
        current_time = time.monotonic()
        delta_time = current_time - self.last_time
        if delta_time == 0:
            delta_time = 1e-9
        self.last_time = current_time
        error = self.setpoint - self.current()
        # print(error)
        self.error_i += error
        if math.isinf(self.error_i):
            raise OverflowError("error_i has overflowed, please tune your PID")
        print(self.error_i)
        output = (
            self.kp * error
            + self.ki * self.error_i
            + self.kd * self.last_error / delta_time
        )
        # clamp output within bounds
        # print(output)
        output = min(max(output, self.minimum), self.minimum)
        return output
