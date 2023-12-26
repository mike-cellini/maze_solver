from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, window, height):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas()
        self.__canvas.pack()
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
        line.draw(self.__canvas, fill_color)

    def draw_cells(self, cells):
        for cell in cells:
            cell.draw(self.__canvas)


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


def draw_test_pattern(win):
    cells = []
    k = 0
    for i in range(1, 5):
        for j in range(1, 5):
            x1 = i * 50
            y1 = j * 50
            top = k & 1 == 1
            right = k & 2 == 2
            bottom = k & 4 == 4
            left = k & 8 == 8
            cells.append(Cell(x1, y1, x1+25, y1+25, top, right, bottom, left, win))
            k += 1
    win.draw_cells(cells)
    for i in range(1, len(cells)):
        cells[i-1].draw_move(cells[i])


def main():
    win = Window(800, 600)
    draw_test_pattern(win)
    win.wait_for_close()


main()
