from cell import Cell
from window import Window

def main():
    win = Window(800, 600)
    c1, c2 = Cell(win), Cell(win)
    c1.draw(20, 30)
    c2.draw(500, 300)
    c1.draw_move(c2, True)
    win.wait_for_close()

if __name__ == "__main__":
    main()