from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        """initiates class ScoreBoard, inherits from Turtle super class, sets initial score to zero, shows ScoreBoard
        on Screen by calling update_scoreboard"""
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-550, 360)
        self.update_scoreboard()

    def update_scoreboard(self):
        """clears ScoreBoard and writes new ScoreBoard with current score"""
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align="left", font=FONT)

    def increase_score(self):
        """increases current score by one, calls update_scoreboard to show current score on Screen"""
        self.score += 1
        self.update_scoreboard()

    def win_game(self):
        """shows banner with YOU WIN on middle of Screen"""
        self.goto(0, 0)
        self.write(f"YOU WIN\nYour score is {self.score}", align="justify", font=FONT)

    def update_high_score(self):
        """updates the high score, if current score is higher than saved high score"""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
            self.score = 0
            self.update_scoreboard()

