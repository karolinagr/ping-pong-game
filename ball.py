from turtle import Turtle


class Ball(Turtle):
    """Create ball and their attributes."""

    def __init__(self):
        # Create ball.
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("DeepPink")
        self.penup()
        self.move_speed = 0.1
        self.x_move = 10
        self.y_move = 10

    def move(self):
        # Create the way how ball moves.
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce(self):
        # Change ball behave after collision with wall.
        self.y_move *= -1

    def bounce_paddle(self):
        # Change ball behave after collision with paddle.
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        # Reset ball position when it misses.
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_paddle()
