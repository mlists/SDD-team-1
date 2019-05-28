import StarLAB
import time

rover = StarLAB.Connect(IP="192.168.1.2")
rover.enableRover()

notes = {
    "F#4": 370,
    "A4": 440,
    "Ab4": 415,
    "B4": 494,
    "E5": 659,
    "D5": 587,
    "C#5": 554,
    "C5": 523,
    "R": 0,
    }


def play(note: str, duration: float = 0.2):
    start_time = time.monotonic()
    current_time = start_time
    # timer setup
    while current_time < (start_time + duration):
        rover.buzzer.setFrequency(notes[note])
        current_time = time.monotonic()
    else:
        rover.buzzer.setFrequency(0)

while True:
    play("R")
    play("B4")
    play("B4")
    play("R")
    play("A4")
    play("A4")
    play("R")
    play("Ab4")
    play("Ab4")
    play("R")
    play("F#4")
    play("F#4")
    play("R")
    play("R")
    play("R")
    play("R")
    play("R")
    play("B4")
    play("B4")
    play("R")
    play("A4")
    play("A4")
    play("R")
    play("Ab4")
    play("Ab4")
    play("R")
    play("F#4")
    play("F#4")
    play("R")
    play("R")
    play("R")
    play("R")
    play("R")
    play("E5")
    play("E5")
    play("R")
    play("D5")
    play("D5")
    play("R")
    play("C#5")
    play("C#5")
    play("R")
    play("B4")
    play("B4")
    play("R")
    play("R")
    play("R")
    play("R")
    play("R")
    play("E5")
    play("E5")
    play("R")
    play("D5")
    play("D5")
    play("R")
    play("C5")
    play("C5")
    play("R")
    play("B4")
    play("B4")
    play("R")
    play("R")
    play("R")
    play("R")
