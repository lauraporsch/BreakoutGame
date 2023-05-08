from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        """initiates class ScoreBoard, inherits from Turtle super class, sets initial score to zero, shows ScoreBoard
        on Screen by calling update_scoreboard"""
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-550, 360)
        self.update_scoreboard()

    def update_scoreboard(self):
        """clears ScoreBoard and writes new ScoreBoard with current score"""
        self.clear()
        self.write(f"Score: {self.score}", align="left", font=FONT)

    def increase_score(self):
        """increases current score by one, calls update_scoreboard to show current score on Screen"""
        self.score += 1
        self.update_scoreboard()

    def win_game(self):
        """shows banner with YOU WIN on middle of Screen"""
        self.goto(0, 0)
        self.write("YOU WIN", align="center", font=FONT)
