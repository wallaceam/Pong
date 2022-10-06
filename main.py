from turtle import Screen, Turtle
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard


def draw_midline():
    midline = Turtle()
    midline.color("white")
    midline.penup()
    midline.setpos(x=0, y=280)
    midline.setheading(270)
    midline.pendown()
    midline.pensize(5)
    midline.ht()
    for _ in range(28):
        midline.forward(10)
        midline.penup()
        midline.forward(10)
        midline.pendown()


screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)
draw_midline()

# Setup
paddle_2 = Paddle()
paddle_1 = Paddle()
paddle_1.goto(-350, 0)

ball = Ball()

scoreboard = Scoreboard()

# Controls
screen.listen()
screen.onkey(paddle_2.move_up, "Up")
screen.onkey(paddle_2.move_down, "Down")
screen.onkey(paddle_1.move_up, "a")
screen.onkey(paddle_1.move_down, "z")

# Gameplay
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect wall bounce
    if ball.ycor() <= -300 or ball.ycor() >= 300:
        ball.wall_bounce()

    # Detect paddle bounce
    if ball.distance(paddle_1) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    if ball.distance(paddle_2) < 50 and ball.xcor() > 320:
        ball.paddle_bounce()

    # Detect point scored
    if ball.xcor() <= -380:
        scoreboard.point_player_2()
        ball.home()
        paddle_1.goto(-350, 0)
        paddle_2.goto(350, 0)
        ball.move_speed = 0.05

    if ball.xcor() >= 380:
        scoreboard.point_player_1()
        ball.home()
        paddle_1.goto(-350, 0)
        paddle_2.goto(350, 0)
        ball.move_speed = 0.05

screen.exitonclick()
