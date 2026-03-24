import random
import Parameters
from tkinter import *

class Food:
    
    def __init__(self, canvas):
        self.canvas = canvas
        self.coordinates = [0, 0]
        self.refresh()
    
    def refresh(self):

        self.canvas.delete("food")
        x = random.randint(0, (Parameters.GAME_WIDTH // Parameters.SPACE_SIZE) - 1) * Parameters.SPACE_SIZE
        y = random.randint(0, (Parameters.GAME_HEIGHT // Parameters.SPACE_SIZE) - 1) * Parameters.SPACE_SIZE

        self.coordinates = [x, y]

        self.canvas.create_oval(x, y, x + Parameters.SPACE_SIZE, y + Parameters.SPACE_SIZE, fill=Parameters.FOOD_COLOR, tag="food")
