import unittest
from screen import Screen


class TestScreen(unittest.TestCase):

    def setUp(self):
        self.screen = Screen(3, 7)

    def test_rect(self):
        self.screen.rect(3, 2)
        expected = """###....
                      ###....
                      .......""".replace(" ", "")
        self.assertEqual(str(self.screen), expected)

    def test_col_shift(self):
        self.screen.rect(3, 2)
        self.screen.col_shift(1, 1)
        expected = """#.#....
                      ###....
                      .#.....""".replace(" ", "")
        self.assertEqual(str(self.screen), expected)

    def test_row_shift(self):
        self.screen.rect(3, 2)
        self.screen.col_shift(1, 1)
        self.screen.row_shift(0, 4)
        expected = """....#.#
                     ###....
                     .#.....""".replace(" ", "")
        self.assertEqual(str(self.screen), expected)

    def test_col_shift_overlap(self):
        self.screen.rect(3, 2)
        self.screen.col_shift(1, 1)
        self.screen.row_shift(0, 4)
        expected = """....#.#
                      ###....
                      .#.....""".replace(" ", "")
        self.assertEqual(str(self.screen), expected)

    def test_command(self):
        self.screen.command("rect 3x2")
        expected = """###....
                      ###....
                      .......""".replace(" ", "")
        self.assertEqual(str(self.screen), expected)


if __name__ == '__main__':
    unittest.main()
