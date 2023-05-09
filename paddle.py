from turtle import Turtle


class Paddle(Turtle):
    """initiates class Paddle, inherits from Turtle super class, sets shape and color of Paddle"""
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=8)
        # hinder to draw on screen, when moving
        self.penup()
        self.color("white")
        self.setpos(0, -300)

    def go_right(self):
        """checks x position of paddle and hinders movement off the screen to right, if still in range, moves paddle 20
        pixels to the right"""
        if self.xcor() > 490:
            pass
        else:
            new_xcor = self.xcor() + 30
            self.goto(y=self.ycor(), x=new_xcor)

    def go_left(self):
        """checks x position of paddle and hinders movement off the screen to left, if still in range, moves paddle 20
        pixels to the left"""
        if self.xcor() < -490:
            pass
        else:
            new_xcor = self.xcor() - 30
            self.goto(y=self.ycor(), x=new_xcor)

    def center_paddle(self):
        """resets paddle position to center"""
        self.goto(0, -300)
