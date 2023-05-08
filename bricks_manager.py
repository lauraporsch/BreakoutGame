from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class BricksManager:
    def __init__(self, pos_x, pos_y):
        """creates wall of bricks on screen"""
        self.all_bricks = []
        self.index = 0
        self.lines_of_bricks = range(len(COLORS))
        self.brick_x = pos_x
        self.brick_y = pos_y
        for color in self.lines_of_bricks:
            for bricks in range(17):
                self.create_brick(position=(self.brick_x, self.brick_y), brick_color=COLORS[self.index])
                self.brick_x += 70
            self.index += 1
            self.brick_y -= 40
            if color % 2 != 0:
                self.brick_x = pos_x
            else:
                self.brick_x = pos_x + 30

    def create_brick(self, position, brick_color):
        """creates a single brick"""
        brick = Turtle("square")
        brick.shapesize(stretch_wid=1.5, stretch_len=3)
        brick.color(brick_color)
        brick.penup()
        brick.goto(position)
        self.all_bricks.append(brick)


