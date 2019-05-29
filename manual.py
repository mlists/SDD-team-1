import tkinter as tk

import StarLAB

from music import Music

rover = StarLAB.Connect(IP="192.168.1.12")
rover.enableRover()

drive_straight_difference = 3  # subtracted from the right motor to try to maintain a straight course

music = Music(rover)  # create an instance of the music class

def key(event):
    if event.char == event.keysym:  # a regular key
        if event.keysym == "m":
            music.tunes()
    else:
        if event.keysym == "up":
            rover.motors.setMotorPower(100 - drive_straight_difference, 100)
        elif event.keysym == "left":
            rover.motors.setMotorPower(-100, 100)
        elif event.keysym == "right":
            rover.motors.setMotorPower(100, -100)
        if event.keysym == "down":
            rover.motors.setMotorPower(-100 + drive_straight_difference, -100)
        

root = tk.Tk()  # initialise tkinter object
print(">>Manual Controls Enabled, Use Arrow Keys To Drive, M For Music<<")
root.bind_all("<Key>", key)  # bind keys to function
root.mainloop()  # run input processing loop
