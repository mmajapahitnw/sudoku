from configs import *
import pygame as pg

pg.init()

class Cells:
    cell_font = pg.font.Font('assets/BaiJamjuree-Bold.ttf', 30)
    cells = []
    # create placeholder for real coords
    for i in range(9):
        row = []
        for j in range(9):
            cell = [0, 0, 0, None, None]
            row.append(cell)
        cells.append(row)
    # generating coordinates
    for i in range(9):
        for j in range(9):
            if i == 0 and j == 0:
                cells[i][j][0] = grid_start[0]
                cells[i][j][1] = grid_start[1]
            else:
                if i == 0:
                    cells[i][j][1] = grid_start[1]
                    cells[i][j][0] = cells[i][j - 1][0] + cell_size + small_pad
                elif j == 0:
                    cells[i][j][0] = grid_start[0]
                    cells[i][j][1] = cells[i - 1][j][1] + cell_size + small_pad
                else:
                    cells[i][j][0] = cells[i][j - 1][0] + cell_size + small_pad
                    cells[i][j][1] = cells[i - 1][j][1] + cell_size + small_pad
                if i == 3 or i == 6:
                    cells[i][j][1] += small_pad * 2
                if j == 3 or j == 6:
                    cells[i][j][0] += small_pad * 2