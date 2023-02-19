from turtle import Turtle
FONT = ("Courier", 20, 'bold')



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(-300, 250)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'score: {self.score}', align='center', font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()