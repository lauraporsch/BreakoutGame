from turtle import Turtle
import random
import time

STARTING_SPEED = 0.09
STARTING_POSITION = (0, -200)
LEFT_OR_RIGHT = [-1, -0.9, -0.8, -0.7, -0.5, -0.3, 0, 0.3, 0.5, 0.7, 0.8, 0.9, 1]


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
        # randomise angle that the ball bounces off
        self.x_move = 15 * random.choice(LEFT_OR_RIGHT)
        # sets time that screen sleeps -> impression of moving ball (while actually just slowly changing coordinates)
        # the smaller move_speed, the faster the ball
        self.move_speed = STARTING_SPEED

    def move(self):
        """makes Ball move on screen by constantly changing coordinates"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """makes Ball bounce off by changing direction on y-axis, gets called when Ball hits upper screen limit"""
        self.y_move *= -1

    def bounce_y_random(self):
        """makes Ball bounce off by changing direction on y-axis, random angle for x-axis, gets called when Ball hits
        a brick """
        self.y_move *= -1
        self.x_move = 15 * random.choice(LEFT_OR_RIGHT)

    def bounce_y_straight(self):
        """makes Ball bounce off by changing direction on y-axis, straight off x-axis, gets called when Ball hits middle
        part of paddle"""
        self.y_move *= -1
        self.x_move = 0

    def bounce_y_left_wide(self):
        """Ball bounces off by changing direction on y-axis, Ball bounces with wide angle towards left on x-axis, gets
        called when Ball hits far left side of paddle"""
        self.y_move *= -1
        self.x_move = 15 * random.choice([-1, -0.9, -0.8, -0.7])

    def bounce_y_left_narrow(self):
        """Ball bounces off by changing direction on y-axis, Ball bounces with narrow angle towards left on x-axis, gets
        called when Ball hits middle left side of paddle"""
        self.y_move *= -1
        self.x_move = 15 * random.choice([-0.5, -0.3, -0.2])

    def bounce_y_right_wide(self):
        """Ball bounces off by changing direction on y-axis, Ball bounces with wide angle towards right on x-axis, gets
        called when Ball hits far right side of paddle"""
        self.y_move *= -1
        self.x_move = 15 * random.choice([0.7, 0.8, 0.9, 1])

    def bounce_y_right_narrow(self):
        """Ball bounces off by changing direction on y-axis, Ball bounces with narrow angle towards right on x-axis, gets
        called when Ball hits middle right side of paddle"""
        self.y_move *= -1
        self.x_move = 15 * random.choice([0.2, 0.3, 0.5])

    def bounce_x(self):
        """Ball bounces off by changing direction on x-axis, gets called when Ball hits side limit of screen"""
        self.x_move *= -1

    def reset_position(self):
        """Ball starts moving from initial position with random movement along x_axis"""
        time.sleep(1)
        self.setpos(STARTING_POSITION)
        self.bounce_y_random()
        self.x_move = 15 * random.choice(LEFT_OR_RIGHT)

    def increase_speed(self):
        """multiplies current move_speed with 0.9 to increase speed"""
        self.move_speed *= 0.9
