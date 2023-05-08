from turtle import Turtle

FONT = ("Courier", 50, "normal")


class LifeBoard(Turtle):
    def __init__(self):
        """initiates class LifeBoard, inherits from Turtle super class, sets initial lives to 3, shows LifeBoard
        on Screen, by calling update_lives"""
        super().__init__()
        self.lives = 3
        self.color("red")
        self.hideturtle()
        self.penup()
        self.goto(550, 325)
        self.update_lives()

    def update_lives(self):
        """clears LifeBoard and writes new LifeBoard with current lives, changes lives to hearts"""
        self.clear()
        current_lives = ""
        for heart in range(self.lives):
            current_lives += "❤️"
        self.write(f"{current_lives}", align="right", font=FONT)

    def decrease_lives(self):
        """decreases current lives by one, calls update_lives to show current lives on Screen"""
        self.lives -= 1
        self.update_lives()

    def game_over(self):
        """shows banner with GAME OVER on middle of Screen"""
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)


