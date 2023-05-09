from turtle import Turtle

Y_POSITION = -300
PADDLE_SIZE = 60
PADDLE_PARTS = []
# create a list of starting positions to create a paddle out of single segments (better detection of distance to paddle)
for x_position in range(-PADDLE_SIZE, PADDLE_SIZE + 10, 10):
    new_part = (x_position, Y_POSITION)
    PADDLE_PARTS.append(new_part)


class Paddle:
    """initiates class Paddle, combines the single parts to one paddle, sets right and left corner of paddle"""
    def __init__(self):
        self.parts = []
        self.create_parts()
        self.right_lead = self.parts[len(PADDLE_PARTS) - 1]
        self.left_lead = self.parts[0]

    def create_parts(self):
        """creates a part for all positions in PADDLE_PARTS, adds them to a list called parts to create a paddle """
        for position in PADDLE_PARTS:
            part = Turtle(shape="square")
            part.color("white")
            part.penup()
            part.goto(position)
            part.shapesize(stretch_wid=0.5)
            self.parts.append(part)

    def go_right(self):
        """checks x position of right corner of paddle and hinders movement off the screen to right, if still in range,
        moves all paddle parts 30 pixels to the right"""
        if self.right_lead.xcor() > 580:
            pass
        else:
            for part in self.parts:
                new_xcor = part.xcor() + 30
                part.goto(y=-300, x=new_xcor)

    def go_left(self):
        """checks x position of left corner of paddle and hinders movement off the screen to right, if still in range,
        moves all paddle parts 30 pixels to the left"""
        if self.left_lead.xcor() < -580:
            pass
        else:
            for part in self.parts:
                new_xcor = part.xcor() - 30
                part.goto(y=-300, x=new_xcor)

    def center_paddle(self):
        """resets paddle position to center"""
        index = 0
        for part in self.parts:
            part.goto(PADDLE_PARTS[index])
            index += 1

