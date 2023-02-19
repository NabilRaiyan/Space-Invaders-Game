import turtle
import winsound


class Player:
    def __init__(self):
        self.bullets_list = []

        self.player = turtle.Turtle()
        turtle.register_shape('assets/Rocket.gif')
        self.player.shape('assets/Rocket.gif')
        self.player.penup()

        self.player.goto(0, -240)

        self.movement = 25

    def move_right(self):
        new_xcor = self.player.xcor() + self.movement
        self.player.goto(new_xcor, self.player.ycor())

    def move_left(self):
        new_x = self.player.xcor() - self.movement
        self.player.goto(new_x, self.player.ycor())

    def create_bullets(self):
        bullet = turtle.Turtle("square")
        bullet.shapesize(stretch_len=0.2, stretch_wid=0.1)
        bullet.penup()
        bullet.color('yellow')
        bullet.setheading(90)
        bullet.goto(self.player.xcor(), self.player.ycor() + 15)
        winsound.PlaySound('sounds/shoot-sound.wav', winsound.SND_ASYNC)
        self.bullets_list.append(bullet)




    def shoot(self):
        for bullet in self.bullets_list:
            bullet.forward(20)
