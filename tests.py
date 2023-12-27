import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10)
        self.assertEqual(
                len(m1._cells),
                num_cols)
        self.assertEqual(
                len(m1._cells[0]),
                num_rows)

        first_cell = m1._cells[0][0]
        self.assertEqual(first_cell._x1, 0)
        self.assertEqual(first_cell._y1, 0)
        self.assertEqual(first_cell.top, False)

        last_cell = m1._cells[num_cols-1][num_rows-1]
        self.assertEqual(last_cell._x2, num_cols * 10)
        self.assertEqual(last_cell._y2, num_rows * 10)
        self.assertEqual(last_cell.bottom, False)


if __name__ == "__main__":
    unittest.main()
