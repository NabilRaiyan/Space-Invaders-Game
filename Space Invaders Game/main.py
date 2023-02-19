# Importing module and files
from turtle import Screen
import time
from enemy import Enemy
from player import Player
from scoreboard import ScoreBoard
from health import Health

# Setting up the screen and creating objects
screen = Screen()

screen.setup(width=800, height=600)
screen.listen()
screen.tracer(0)
screen.title("Space Invaders")
screen.bgcolor('black')
screen.bgpic('assets/galaxy-bg-2.gif')

# Creating Rocket object
rocket = Player()
score = ScoreBoard()
enemy = Enemy()
health = Health()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    # Rocket moving
    screen.onkey(key="Right", fun=rocket.move_right)
    screen.onkey(key="Left", fun=rocket.move_left)

    # Shooting mechanism
    screen.onkey(key='s', fun=rocket.create_bullets)

    rocket.shoot()
    enemy.shoot()

    # Creating enemy and enemy movement
    enemy.create_enemy()
    enemy.move_enemy()

    # Detecting collision of bullets with enemy
    for bullet in rocket.bullets_list:
        for e in enemy.enemy_list:
            if bullet.distance(e) < 20:
                enemy.enemy_list.remove(e)
                e.hideturtle()
                score.increase_score()

    # Detecting collision of enemy bullets with player
    for bullet in enemy.enemy_bullet_list:
        if bullet.distance(rocket.player) < 20 and bullet.ycor() < -250:
            health.decrease_health()
            if health.health == 0:
                health.game_over()
                game_is_on = False

    # Detecting collision of enemy with player
    for e in enemy.enemy_list:
        if e.distance(rocket.player) < 20 and e.ycor() < -250:
            health.decrease_health()
            if health.health == 0:
                health.game_over()
                game_is_on = False

screen.mainloop()
