import time

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

class Music():

    def __init__(self, rover):
        self.rover = rover

    def play(self: self, note: str, duration: float = 0.2):
        start_time = time.monotonic()
        current_time = start_time
        # timer setup
        while current_time < (start_time + duration):
            self.rover.buzzer.setFrequency(notes[note])
            current_time = time.monotonic()
        else:
            self.rover.buzzer.setFrequency(0)

    def tunes(self):
        while True:
            self.play("R")
            self.play("B4")
            self.play("B4")
            self.play("R")
            self.play("A4")
            self.play("A4")
            self.play("R")
            self.play("Ab4")
            self.play("Ab4")
            self.play("R")
            self.play("F#4")
            self.play("F#4")
            self.play("R")
            self.play("R")
            self.play("R")
            self.play("R")
            self.play("R")
            self.play("B4")
            self.play("B4")
            self.play("R")
            self.play("A4")
            self.play("A4")
            self.play("R")
            self.play("Ab4")
            self.play("Ab4")
            self.play("R")
            self.play("F#4")
            self.play("F#4")
            self.play("R")
            self.play("R")
            self.play("R")
            self.play("R")
            self.play("R")
            self.play("E5")
            self.play("E5")
            self.play("R")
            self.play("D5")
            self.play("D5")
            self.play("R")
            self.play("C#5")
            self.play("C#5")
            self.play("R")
            self.play("B4")
            self.play("B4")
            self.play("R")
            self.play("R")
            self.play("R")
            self.play("R")
            self.play("R")
            self.play("E5")
            self.play("E5")
            self.play("R")
            self.play("D5")
            self.play("D5")
            self.play("R")
            self.play("C5")
            self.play("C5")
            self.play("R")
            self.play("B4")
            self.play("B4")
            self.play("R")
            self.play("R")
            self.play("R")
            self.play("R")
