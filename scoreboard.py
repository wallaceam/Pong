from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player_1_score = 0
        self.player_2_score = 0
        self.ht()
        self.penup()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.player_1_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.player_2_score, align="center", font=("Courier", 60, "normal"))

    def point_player_1(self):
        self.player_1_score += 1
        self.update_scoreboard()

    def point_player_2(self):
        self.player_2_score += 1
        self.update_scoreboard()
