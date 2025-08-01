from time import sleep
from cell import Cell

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        win,
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
        sleep(.01)