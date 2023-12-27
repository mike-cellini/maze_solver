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
