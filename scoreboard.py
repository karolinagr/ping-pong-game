from turtle import Turtle


class Scoreboard(Turtle):
    """Count a show acctual score of each player."""

    def __init__(self, x, y):
        # Create a scoreboard.
        super().__init__()
        self.color("DeepPink")
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.score = 0
        self.score_information()

    def score_information(self):
        # Show on screen acctual score.
        self.write(self.score, align='center', font=('Arial', 20, 'bold'))

    def add_score(self):
        # Add point.
        self.score += 1
        self.clear()
