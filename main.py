from Food import Food
from Snake import Snake
from Game_Logic import Game_logic
import Parameters
from tkinter import *

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = "down"
label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=Parameters.BACKGROUND_COLOR, height=Parameters.GAME_HEIGHT, width=Parameters.GAME_WIDTH)
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