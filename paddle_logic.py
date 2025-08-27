class PaddleLogic:
    """Logic for paddle movement without graphics."""

    def __init__(self, x, y, step=10, limit=240):
        self.x = x
        self.y = y
        self.step = step
        self.limit = limit

    def up(self):
        """Move paddle up, respecting upper boundary."""
        if self.y < self.limit:
            self.y += self.step

    def down(self):
        """Move paddle down, respecting lower boundary."""
        if self.y > -self.limit:
            self.y -= self.step

    def position(self):
        """Return current position as tuple (x, y)."""
        return self.x, self.y
