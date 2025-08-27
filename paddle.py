# from turtle import Turtle
#
#
# class Paddle(Turtle):
#     """Create paddle and its attributes."""
#
#     def __init__(self, position, color="#F46A00"):
#         # Create paddle.
#         super().__init__()
#         self.shape("square")
#         self.penup()
#         self.shapesize(stretch_wid=5, stretch_len=0.5)
#         self.color(color)
#         self.goto(position)
#
#     def up(self):
#         # Move paddle up.
#         x_position = self.xcor()
#         y_position = self.ycor()
#         if 240 >= y_position:
#             self.goto(x=x_position, y=y_position + 10)
#
#     def down(self):
#         # Move paddle down.
#         x_position = self.xcor()
#         y_position = self.ycor()
#         if y_position >= -240:
#             self.goto(x=x_position, y=y_position - 10)



from turtle import Turtle
from paddle_logic import PaddleLogic


class Paddle(Turtle):
    """Graphical paddle using Turtle, backed by PaddleLogic."""

    def __init__(self, position, color="#F46A00"):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=0.5)
        self.color(color)
        self.goto(position)

        # logika ruchu
        self.logic = PaddleLogic(*position)

    def up(self):
        self.logic.up()
        self.goto(self.logic.x, self.logic.y)

    def down(self):
        self.logic.down()
        self.goto(self.logic.x, self.logic.y)
