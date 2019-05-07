import StarLAB

from pid import PID

rover = StarLAB.Connect(IP="192.168.1.12")
rover.enableRover()

print(rover.IMU.getOrientation())


def read_imu():
    return rover.IMU.getOrientation()[2]


pid = PID(read_imu)

pid.set_gains(kp=0.5, ki=0, kd=0.0, kf=0.0)
pid.set_range(minimum=-100, maximum=100)

pid.set_setpoint(rover.IMU.getOrientation())

while True:
    output = pid.get()
    rover.motors.setMotorPower(output, -output)
