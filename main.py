from cell import Cell
from window import Window

def main():
    win = Window(800, 600)
    c = Cell(win)
    c.draw(20, 30)
    win.wait_for_close()

if __name__ == "__main__":
    main()