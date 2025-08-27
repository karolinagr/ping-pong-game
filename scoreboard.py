from turtle import Turtle


class Scoreboard(Turtle):
    """Count a show acctual score of each player."""

    def __init__(self, x, y, color="#F46A00"):
        # Create a scoreboard.
        super().__init__()
        self.color(color)
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.score = 0
        self.score_information()

    def score_information(self):
        # Show on screen actual score.
        self.write(self.score, align='center', font=('Comic', 20, 'bold'))

    def add_score(self):
        # Add point.
        self.score += 1
        self.clear()
