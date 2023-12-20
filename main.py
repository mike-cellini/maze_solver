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


def main():
    win = Window(800, 600)
    points = [
        Point(50, 50),
        Point(50, 100),
        Point(100, 100)]
    for i in range(1, len(points)):
        print(f"{i}")
        win.draw_line(Line(points[i-1], points[i]), "black")
    win.wait_for_close()


main()
