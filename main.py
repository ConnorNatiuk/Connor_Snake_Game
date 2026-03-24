from Food import Food
from Snake import Snake
from Game_Logic import Game_logic
from tkinter import *
import random

GAME_WIDTH = 800
GAME_HEIGHT = 800
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#FF69B4"
FOOD_COLOR = "#8F1402"
BACKGROUND_COLOR = "#111184"

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = "down"
label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_height/2) - (window_height/2))
y = int((screen_width/2) - (window_width/2))

window.geometry(f"{window_width}x{window_height}+{y}+{x}")

snake = Snake(canvas)
food = Food(canvas)

window.mainloop()
def main():
    pass