import time
import tkinter as tk

import StarLAB

from music import Music

rover = StarLAB.Connect(IP="192.168.1.12")
rover.enableRover()

drive_straight_difference = 3  # subtracted from the right motor to try to maintain a straight course

music = Music(rover)  # create an instance of the music class

def spin(motor_value: int, duration: float) -> None:
    """
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
    rover.motors.setMotorPower(0, 0)


def drive(motor_value: int, duration: float) -> None:
    """
    Run the motors in the same direction to drive forwards.
    Param: motor_value - a posative or negative percentage to drive both motors at.
    Param: duration - time in seconds to drive for.
    """
    if motor_value > 100 or motor_value < -100:
        # confirm the values are within bounds
        raise ValueError

    start_time = time.monotonic()
    current_time = start_time
    # timer setup

    while current_time < (start_time + duration):
        current_time = time.monotonic()
        rover.motors.setMotorPower(motor_value - drive_straight_difference, motor_value)
    rover.motors.setMotorPower(0, 0)

def key(event):
    if event.char == event.keysym:  # a regular key
        if event.keysym == "m":
            music.tunes()
    else:
        if event.keysym == "up":
            drive(100, 0.1)
        elif event.keysym == "left":
            spin(100, 0.1)
        elif event.keysym == "right":
            spin(-100, 0.1)
        if event.keysym == "down":
            drive(-100, 0.1)
        

root = tk.Tk()  # initialise tkinter object
print(">>Manual Controls Enabled, Use Arrow Keys To Drive, M For Music<<")
root.bind_all("<Key>", key)  # bind keys to function
root.mainloop()  # run input processing loop
