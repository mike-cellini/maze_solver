from cell import Cell
import random
import time


class Maze:
    def __init__(
            self,
            x,
            y,
            num_rows,
            num_cols,
            cell_size,
            win=None,
            seed=None,
    ):
        self._cells = None
        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size = cell_size
        self._win = win
        self._create_cells()
        self._break_entrance_and_exit()
        if seed is not None:
            random.seed(seed)
        self._break_walls_r(0, 0)

    def _create_cells(self):
        self._cells = []
        for i in range(0, self._num_cols):
            col = []
            for j in range(0, self._num_rows):
                x1 = self._x + i * self._cell_size
                y1 = self._y + j * self._cell_size
                x2 = x1 + self._cell_size
                y2 = y1 + self._cell_size
                cell = Cell(x1, y1, x2, y2, True, True, True, True, self._win)
                col.append(cell)
            self._cells.append(col)

        for i in range(0, self._num_cols):
            for j in range(0, self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        self._cells[i][j].draw(self._win.canvas)
        self._animate()

    def _animate(self):
        if not self._win:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        entrance.top = False
        self._draw_cell(0, 0)

        exit_col = self._num_cols - 1
        exit_row = self._num_rows - 1
        exitcell = self._cells[exit_col][exit_row]
        exitcell.bottom = False
        self._draw_cell(exit_col, exit_row)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i > 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1, j))
            if j < len(self._cells[i]) - 1 and not self._cells[i][j+1].visited:
                to_visit.append((i, j+1))
            if i < len(self._cells) - 1 and not self._cells[i+1][j].visited:
                to_visit.append((i+1, j))
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit.append((i, j-1))
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            k = random.randrange(0, len(to_visit), 1)
            visit_coord = to_visit[k]
            here = self._cells[i][j]
            there = self._cells[visit_coord[0]][visit_coord[1]]
            if i > visit_coord[0]:
                print("Break right")
                here.left = False
                there.right = False
            elif j < visit_coord[1]:
                print("Break bottom")
                here.bottom = False
                there.top = False
            elif i < visit_coord[0]:
                print("Break left")
                here.right = False
                there.left = False
            elif j > visit_coord[1]:
                print("Break top")
                here.top = False
                there.bottom = False
            print(f"Visiting {visit_coord[0]}, {visit_coord[1]}")
            self._draw_cell(i, j)
            self._break_walls_r(visit_coord[0], visit_coord[1])
