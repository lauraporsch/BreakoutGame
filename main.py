from turtle import Screen
from paddle import Paddle
from lifeboard import LifeBoard
from ball import Ball
from bricks_manager import BricksManager
from scoreboard import Scoreboard
import time


X_BORDER_LEFT = -580
BRICKS_HEIGHT = 280
# ----------------------------- UI ------------------------------- #
screen = Screen()
screen.setup(width=1200, height=800)
screen.bgcolor("black")
screen.title("Hit the Bricks")
# turn automatic screen updates off and only trigger by functions
screen.tracer(0)

# set up all elements on the screen
paddle = Paddle()
scoreboard = Scoreboard()
life_board = LifeBoard()
ball = Ball()
bricks_manager = BricksManager(X_BORDER_LEFT, BRICKS_HEIGHT)

# give screen ability to listen to events
screen.listen()
screen.onkeypress(paddle.go_right, "Right")
screen.onkeypress(paddle.go_left, "Left")


def play_game():
    game_is_on = True
    hit_bricks = 0
    while game_is_on:
        # screen sleeps for time that the ball takes to move from one position to the next
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()
        # makes ball bounce off upper screen limit
        if ball.ycor() > 370:
            ball.bounce_y()
        # makes ball bounce off paddle
        for part in paddle.parts:
            if ball.distance(part) < 40 and ball.ycor() < -270:
                ball.bounce_y()
                # break to hinder ball from bouncing on paddle several times
                break
        # makes ball bounce off side screen limits
        if ball.xcor() > 580 or ball.xcor() < -580:
            ball.bounce_x()
        # triggers functions if ball misses paddle
        if ball.ycor() < -350:
            life_board.decrease_lives()
            ball.reset_position()
            paddle.center_paddle()
        # detects when ball hits brick
        for brick in bricks_manager.all_bricks:
            if ball.distance(brick) < 40:
                brick.hideturtle()
                bricks_manager.all_bricks.remove(brick)
                scoreboard.increase_score()
                ball.bounce_y()
                hit_bricks += 1
                # increase ball speed every time after 10 blocks got removed up to a maximum
                if ball.move_speed > 0.04 and hit_bricks != 0 and hit_bricks % 10 == 0:
                    ball.increase_speed()
        # triggers Game Over function when no lives left
        if life_board.lives == 0:
            life_board.game_over()
            game_is_on = False
            scoreboard.update_high_score()
        # triggers Win Game function when no bricks left
        if not bricks_manager.all_bricks:
            scoreboard.win_game()
            game_is_on = False
            scoreboard.update_high_score()


play_game()

# keep screen open until exit button is triggered
screen.exitonclick()
