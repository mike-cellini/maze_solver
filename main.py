from tkinter import Tk, BOTH, Canvas
import time


class Window:
    def __init__(self, window, height):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas()
        self.canvas.pack()
        self.__window_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__window_running = True
        while self.__window_running:
            self.redraw()

    def close(self):
        self.__window_running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

    def draw_cells(self, cells):
        for cell in cells:
            cell.draw(self.canvas)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Line:
    def __init__(self, p1, p2):
        self.points = (p1, p2)

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.points[0].x,
            self.points[0].y,
            self.points[1].x,
            self.points[1].y,
            fill=fill_color,
            width=2)
        canvas.pack()


class Cell:
    def __init__(self, x1, y1, x2, y2, top, right, bottom, left, win):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left
        self.__win = win

    def draw(self, canvas):
        if self.top:
            top_line = Line(
                Point(self.__x1, self.__y1),
                Point(self.__x2, self.__y1))
            self.__win.draw_line(top_line, "black")
        if self.right:
            right_line = Line(
                Point(self.__x2, self.__y1),
                Point(self.__x2, self.__y2))
            self.__win.draw_line(right_line, "black")
        if self.bottom:
            bottom_line = Line(
                Point(self.__x2, self.__y2),
                Point(self.__x1, self.__y2))
            self.__win.draw_line(bottom_line, "black")
        if self.left:
            left_line = Line(
                Point(self.__x1, self.__y2),
                Point(self.__x1, self.__y1))
            self.__win.draw_line(left_line, "black")
        canvas.pack()

    def get_center(self):
        x = (self.__x1 + self.__x2) // 2
        y = (self.__y1 + self.__y2) // 2
        return Point(x, y)

    def draw_move(self, to_cell, undo=False):
        fill_color = "red"
        if undo:
            fill_color = "gray"

        move = Line(self.get_center(), to_cell.get_center())

        self.__win.draw_line(move,
                             fill_color)


class Maze:
    def __init__(
            self,
            x,
            y,
            num_rows,
            num_cols,
            cell_size,
            win,
    ):
        self.__x = x
        self.__y = y
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size = cell_size
        self.__win = win
        self.__create_cells()
        self.__animate()

    def __create_cells(self):
        self.__cells = []
        for i in range(0, self.__num_cols):
            col = []
            for j in range(0, self.__num_rows):
                x1 = self.__x + i * self.__cell_size
                y1 = self.__y + j * self.__cell_size
                x2 = x1 + self.__cell_size
                y2 = y1 + self.__cell_size
                cell = Cell(x1, y1, x2, y2, True, True, True, True, self.__win)
                col.append(cell)
            self.__cells.append(col)

        for i in range(0, self.__num_cols):
            for j in range(0, self.__num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        self.__cells[i][j].draw(self.__win.canvas)

    def __animate(self):
        while True:
            self.__win.redraw()
            time.sleep(0.05)


def main():
    win = Window(800, 600)
    maze = Maze(50, 50, 5, 5, 50, win)
    win.wait_for_close()


main()
