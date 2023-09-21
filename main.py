from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# Set screen attributes.
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Create right paddles.
r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))

# Create ball.
ball = Ball()

# Create scoreboard of each player.
l_scoreboard = Scoreboard(-200, 260)
r_scoreboard = Scoreboard(200, 260)

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()
    # Detect collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    # Detect collision with paddle.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_paddle()
    # Detect when R paddle misses.
    if ball.distance(l_paddle) > 50 and ball.xcor() < -365:
        r_scoreboard.add_score()
        r_scoreboard.score_information()
        ball.reset_position()
    # Detect when L paddle misses.
    if ball.distance(r_paddle) > 50 and ball.xcor() > 365:
        l_scoreboard.add_score()
        l_scoreboard.score_information()
        ball.reset_position()

screen.exitonclick()
