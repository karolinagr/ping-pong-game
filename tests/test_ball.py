import unittest
from ball_logic import BallLogic


class TestBallLogic(unittest.TestCase):
    def setUp(self):
        self.ball = BallLogic()

    def test_initial_state(self):
        self.assertEqual((self.ball.x, self.ball.y), (0, 0))
        self.assertEqual(self.ball.x_move, 10)
        self.assertEqual(self.ball.y_move, 10)
        self.assertEqual(self.ball.move_speed, 0.1)

    def test_move(self):
        self.ball.move()
        self.assertEqual((self.ball.x, self.ball.y), (10, 10))

    def test_bounce(self):
        old_y = self.ball.y_move
        self.ball.bounce()
        self.assertEqual(self.ball.y_move, -old_y)

    def test_bounce_paddle(self):
        old_x = self.ball.x_move
        old_speed = self.ball.move_speed
        self.ball.bounce_paddle()
        self.assertEqual(self.ball.x_move, -old_x)
        self.assertLess(self.ball.move_speed, old_speed)

    def test_reset_position(self):
        self.ball.x, self.ball.y = 100, 50
        self.ball.move_speed = 0.5
        old_x = self.ball.x_move
        self.ball.reset_position()
        self.assertEqual((self.ball.x, self.ball.y), (0, 0))
        self.assertAlmostEqual(self.ball.move_speed, 0.1, places=1)
        self.assertEqual(self.ball.x_move, -old_x)


if __name__ == "__main__":
    unittest.main()
