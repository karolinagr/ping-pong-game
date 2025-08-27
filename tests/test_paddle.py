import unittest
from paddle import Paddle

class TestPaddle(unittest.TestCase):
    def setUp(self):
        self.paddle = Paddle((370,0), color="#F46A00")


    def test_initial_position(self):
        self.assertEqual(self.paddle.position(), (370,0))


    def test_color(self):
        expected = (244 / 255, 106 / 255, 0.0)
        actual = self.paddle.fillcolor()
        for e, a in zip(expected, actual):
            self.assertAlmostEqual(e, a, places=3)


    def test_move_up(self):
        y_position = self.paddle.ycor()
        self.paddle.up()
        y_position_next = self.paddle.ycor()
        self.assertEqual(y_position, y_position_next - 10)


    def test_move_down(self):
        y_position = self.paddle.ycor()
        self.paddle.down()
        y_position_next = self.paddle.ycor()
        self.assertEqual(y_position, y_position_next + 10)

if __name__ == '__main__':
    unittest.main()