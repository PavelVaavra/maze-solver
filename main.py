from cell import Line, Point
from window import Window

def main():
    win = Window(800, 600)
    line1 = Line(Point(10, 10), Point(790, 590))
    win.draw_line(line1, "red")
    line2 = Line(Point(10, 590), Point(790, 10))
    win.draw_line(line2)
    win.wait_for_close()

if __name__ == "__main__":
    main()