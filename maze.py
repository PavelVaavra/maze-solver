from time import sleep
from cell import Cell

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        win=None,
        cell_size_x=40,
        cell_size_y=40
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        self.__cells = [[Cell(self.__win) for i in range(self.__num_rows)] for j in range(self.__num_cols)]
        if self.__win:
            for i in range(self.__num_cols):
                for j in range(self.__num_rows):
                    self.__draw_cell(i, j)
        self.__break_entrance_and_exit()

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
        self.__draw_cell(0, 0)
        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)