from cell import Cell
from window import Window
from maze import Maze

def main():
    win = Window(800, 600)
    m = Maze(40, 40, 13, 18, win)
    win.wait_for_close()

if __name__ == "__main__":
    main()