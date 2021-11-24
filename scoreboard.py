from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Tahoma", 15, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_write()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=True, align=ALIGNMENT, font=FONT)

    def score_write(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score = {self.score}", move=True, align=ALIGNMENT, font=FONT)
        self.score += 1
