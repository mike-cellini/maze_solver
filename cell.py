from line import Line
from point import Point


class Cell:
    WALL_COLOR = "black"
    NO_WALL_COLOR = "white"

    def __init__(self, x1, y1, x2, y2, top, right, bottom, left, win=None):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left
        self._win = win
        self.visited = False

    def draw(self):
        if self._win is None:
            return

        top_line = Line(
            Point(self._x1, self._y1),
            Point(self._x2, self._y1))
        if self.top:
            self._win.draw_line(top_line, self.WALL_COLOR)
        else:
            self._win.draw_line(top_line, self.NO_WALL_COLOR)

        right_line = Line(
            Point(self._x2, self._y1),
            Point(self._x2, self._y2))
        if self.right:
            self._win.draw_line(right_line, self.WALL_COLOR)
        else:
            self._win.draw_line(right_line, self.NO_WALL_COLOR)

        bottom_line = Line(
            Point(self._x2, self._y2),
            Point(self._x1, self._y2))
        if self.bottom:
            self._win.draw_line(bottom_line, self.WALL_COLOR)
        else:
            self._win.draw_line(bottom_line, self.NO_WALL_COLOR)

        left_line = Line(
            Point(self._x1, self._y2),
            Point(self._x1, self._y1))
        if self.left:
            self._win.draw_line(left_line, self.WALL_COLOR)
        else:
            self._win.draw_line(left_line, self.NO_WALL_COLOR)

    def get_center(self):
        x = (self._x1 + self._x2) // 2
        y = (self._y1 + self._y2) // 2
        return Point(x, y)

    def draw_move(self, to_cell, undo=False):
        fill_color = "red"
        if undo:
            fill_color = "gray"

        move = Line(self.get_center(), to_cell.get_center())

        self._win.draw_line(move,
                            fill_color)
