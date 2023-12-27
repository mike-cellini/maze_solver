from tkinter import Tk, BOTH, Canvas
from maze import Maze


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


def main():
    win = Window(800, 600)
    maze = Maze(50, 50, 5, 5, 50, win)
    win.wait_for_close()


main()
