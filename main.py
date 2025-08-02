from cell import Cell
from window import Window
from maze import Maze

def main():
    cell_size = 40
    num_rows = 13
    num_cols = 18
    win = Window((num_cols + 2) * cell_size, (num_rows + 2) * cell_size)
    m = Maze(cell_size, cell_size, num_rows, num_cols, win, cell_size, cell_size)
    win.wait_for_close()

if __name__ == "__main__":
    main()