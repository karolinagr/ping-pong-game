class BallLogic:
    """Logic of the ball movement without graphics."""

    def __init__(self, x=0, y=0, x_move=10, y_move=10, move_speed=0.1):
        self.x = x
        self.y = y
        self.x_move = x_move
        self.y_move = y_move
        self.move_speed = move_speed

    def move(self):
        """Update position based on current direction."""
        self.x += self.x_move
        self.y += self.y_move

    def bounce(self):
        """Reverse vertical direction (hit top/bottom wall)."""
        self.y_move *= -1

    def bounce_paddle(self):
        """Reverse horizontal direction and increase speed."""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Reset position and speed after scoring."""
        self.x, self.y = 0, 0
        self.move_speed = 0.1
        self.bounce_paddle()
