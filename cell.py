
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y, 
            self.point2.x, self.point2.y, 
            fill=fill_color, width=2
        )

class Cell():
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, x, y, cell_size_x=50, cell_size_y=50):
        self.__x1 = x
        self.__x2 = x + cell_size_x
        self.__y1 = y
        self.__y2 = y + cell_size_y
        p1 = Point(self.__x1, self.__y1)
        p2 = Point(self.__x2, self.__y1)
        p3 = Point(self.__x2, self.__y2)
        p4 = Point(self.__x1, self.__y2)
        if self.has_top_wall:
            self.__win.draw_line(Line(p1, p2))
        if self.has_right_wall:
            self.__win.draw_line(Line(p2, p3))
        if self.has_bottom_wall:
            self.__win.draw_line(Line(p3, p4))
        if self.has_left_wall:
            self.__win.draw_line(Line(p4, p1))