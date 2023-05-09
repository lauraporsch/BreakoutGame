from turtle import Turtle
import random
import time

SPEED = 0.09
STARTING_POSITION = (0, -200)


class Ball(Turtle):
    def __init__(self):
        """initiates class Ball, inherits from Turtle super class, sets shape and color of Ball, sets ball movement to
        10 pixels up per movement, sets movement on x_axis to random left or right choice and different angles"""
        super().__init__()
        self.shape("circle")
        self.color("white")
        #  no drawing on screen
        self.penup()
        self.setpos(STARTING_POSITION)
        self.y_move = 15
        # list of different directions and angles
        left_or_right = [-1, -0.9, -0.8, -0.7, 0.7, 0.8, 0.9, 1]
        self.x_move = 15 * random.choice(left_or_right)
        # sets time that screen sleeps -> impression of moving ball (while actually just slowly changing coordinates)
        # the smaller move_speed, the faster the ball
        self.move_speed = SPEED

    def move(self):
        """makes Ball move on screen by constantly changing coordinates"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """makes Ball bounce off by changing direction on y-axis """
        self.y_move *= -1
        left_or_right = [-1, -0.9, -0.8, -0.7, 0.7, 0.8, 0.9, 1]
        self.x_move = 15 * random.choice(left_or_right)

    def bounce_x(self):
        """makes Ball bounce off by changing direction on x-axis """
        self.x_move *= -1

    def reset_position(self):
        """ball starts moving from initial position with random movement along x_axis"""
        time.sleep(1)
        self.setpos(STARTING_POSITION)
        self.bounce_y()
        left_or_right = [-1, -0.9, -0.8, -0.7, 0.7, 0.8, 0.9, 1]
        self.x_move = 15 * random.choice(left_or_right)
