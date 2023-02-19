import turtle
from turtle import Turtle

import winsound

FONT = ("Courier", 20, 'bold')


class Health(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(300, 250)
        self.health = 5
        self.update_health()

    def update_health(self):
        self.clear()
        self.write(f'health: {self.health}', align='center', font=FONT)

    def decrease_health(self):
        self.health -= 1
        self.update_health()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 30, "bold"))
        winsound.PlaySound('sounds/game-over.wav', winsound.SND_ASYNC)




