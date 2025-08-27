import unittest
from ball import Ball

class TestBall(unittest.TestCase):
    def setUp(self):
        self.ball = Ball()


    def test_initial_state(self):
        self.assertEqual(self.ball.position(), (0,0))
        self.assertEqual(self.ball.move_speed, 0.1)
        self.assertEqual(self.ball.x_move, 10)
        self.assertEqual(self.ball.y_move, 10)


    def test_move(self):
        self.ball.goto(0,0)
        self.ball.move()
        after_posiotion = self.ball.position()
        self.assertLess(after_posiotion, (10,10))


    def test_bounce(self):
        ball_before_collision = self.ball.y_move
        self.ball.bounce()
        ball_after_collision = self.ball.y_move
        self.assertEqual(ball_before_collision, -ball_after_collision)


    def test_bounce_paddle(self):
        self.ball.goto(0,0)
        x_before_paddle_collision = self.ball.x_move
        speed_before = self.ball.move_speed
        self.ball.bounce_paddle()
        x_after_paddle_collision = self.ball.x_move
        speed_after = self.ball.move_speed
        self.assertEqual(-x_before_paddle_collision, x_after_paddle_collision)
        self.assertEqual(0.9 * speed_before, speed_after)


if __name__ == "__main__":
    unittest.main()
