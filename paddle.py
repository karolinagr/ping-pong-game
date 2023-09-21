from turtle import Turtle


class Paddle(Turtle):
    """Create paddle and its attributes."""

    def __init__(self, position):
        # Create paddle.
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("DeepPink")
        self.goto(position)

    def up(self):
        # Move paddle up.
        x_position = self.xcor()
        y_position = self.ycor()
        if 240 >= y_position:
            self.goto(x=x_position, y=y_position + 10)

    def down(self):
        # Move paddle down.
        x_position = self.xcor()
        y_position = self.ycor()
        if y_position >= -240:
            self.goto(x=x_position, y=y_position - 10)
