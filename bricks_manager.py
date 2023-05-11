from turtle import Turtle

COLORS = ["#FFADAD", "#FFD6A5", "#FDFFB6", "#CAFFBF", "#9BF6FF", "#BDB2FF"]
NUMBER_OF_BRICKS_ROW = 5


class BricksManager:
    def __init__(self, pos_x, pos_y):
        """creates wall of bricks on screen"""
        self.all_bricks = []
        self.index = 0
        self.lines_of_bricks = range(len(COLORS))
        self.brick_x = pos_x
        self.brick_y = pos_y
        # allows changing wall of bricks by simply changing constants
        for color in self.lines_of_bricks:
            for bricks in range(NUMBER_OF_BRICKS_ROW):
                self.create_brick(position=(self.brick_x, self.brick_y), brick_color=COLORS[self.index])
                self.brick_x += 70
            self.index += 1
            self.brick_y -= 40
            # indents every second block by 30 pixels
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


