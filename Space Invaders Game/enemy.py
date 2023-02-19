import turtle
import random

import winsound


class Enemy:
    def __init__(self):
        self.enemy_list = []
        self.enemy_bullet_list = []
        self.enemy_movement = 5

    def create_enemy(self):
        if random.randint(1, 6) == 2:
            enemy = turtle.Turtle()
            turtle.register_shape('assets/enemy.gif')
            enemy.shape('assets/enemy.gif')
            enemy.setheading(270)
            enemy.penup()
            random_x = random.randint(-300, 300)
            random_y = random.randint(200, 400)
            enemy.goto(random_x + 10, random_y + 10)
            self.enemy_list.append(enemy)

            # Creating enemy bullets
            self.enemy_bullet(enemy.xcor(), enemy.ycor())

    def move_enemy(self):
        for enemy in self.enemy_list:
            enemy.forward(self.enemy_movement)

    def enemy_bullet(self, x, y):
        bullet = turtle.Turtle("square")
        bullet.penup()
        bullet.color('yellow')
        bullet.shapesize(stretch_len=0.2, stretch_wid=0.1)
        bullet.goto(x, y)
        winsound.PlaySound('sounds/enemy-shoot sound.wav', winsound.SND_ASYNC)
        self.enemy_bullet_list.append(bullet)

    def shoot(self):
        for bullet in self.enemy_bullet_list:
            bullet.setheading(270)
            bullet.forward(10)
