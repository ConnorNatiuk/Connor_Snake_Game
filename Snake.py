import Parameters
from tkinter import *

class Snake:
    def __init__(self, canvas):
        self.canvas = canvas
        self.body_size = Parameters.BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, Parameters.BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + Parameters.SPACE_SIZE, y + Parameters.SPACE_SIZE, fill=Parameters.SNAKE_COLOR, tag="snake")