from time import sleep
from cell import Cell
import random

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        win=None,
        cell_size_x=40,
        cell_size_y=40,
        seed=None,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        if seed is not None:
            random.seed(seed)
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)

    def __create_cells(self):
        self.__cells = [[Cell(self.__win) for i in range(self.__num_rows)] for j in range(self.__num_cols)]
        if self.__win:
            for i in range(self.__num_cols):
                for j in range(self.__num_rows):
                    self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        self.__cells[i][j].draw(self.__x1 + i * self.__cell_size_x, 
                                self.__y1 + j * self.__cell_size_y,
                                self.__cell_size_x,
                                self.__cell_size_y)
        self.__animate()

    def __animate(self):
        self.__win.redraw()
        sleep(.001)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        if self.__win:
            self.__draw_cell(0, 0)
            self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            possible_directions = []
            # adjacent to the left of the current cell
            if 0 <= i - 1:
                if not self.__cells[i - 1][j].visited:
                    possible_directions.append((i - 1, j))
            # adjacent to the right of the current cell
            if i + 1 < self.__num_cols:
                if not self.__cells[i + 1][j].visited:
                    possible_directions.append((i + 1, j))
            # adjacent on the top of the current cell
            if 0 <= j - 1:
                if not self.__cells[i][j - 1].visited:
                    possible_directions.append((i, j - 1))
            # adjacent under the bottom of the current cell
            if j + 1 < self.__num_rows:
                if not self.__cells[i][j + 1].visited:
                    possible_directions.append((i, j + 1))
            if len(possible_directions) == 0:
                self.__draw_cell(i, j)
                return
            i_new, j_new = possible_directions[random.randrange(len(possible_directions))]
            # same column
            if i == i_new:
                # adjacent above current
                if j > j_new:
                    self.__cells[i][j].has_top_wall = False
                    self.__cells[i_new][j_new].has_bottom_wall = False
                # adjacent under current
                else:
                    self.__cells[i][j].has_bottom_wall = False
                    self.__cells[i_new][j_new].has_top_wall = False
            # same row
            else:
                # adjacent on the right side of current
                if i < i_new:
                    self.__cells[i][j].has_right_wall = False
                    self.__cells[i_new][j_new].has_left_wall = False
                # adjacent on the left side of current
                else:
                    self.__cells[i][j].has_left_wall = False
                    self.__cells[i_new][j_new].has_right_wall = False
            self.__draw_cell(i, j)
            self.__draw_cell(i_new, j_new)
            self.__break_walls_r(i_new, j_new)