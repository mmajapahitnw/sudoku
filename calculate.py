import pygame as pg
from cells import Cells
from configs import *

def is_valid(row, col, num, n):
    print(f'{row}, {col}')
    for i in range(n):
        if Cells.cells[row][i][2] == num:
            return False

    for i in range(n):
        if Cells.cells[i][col][2] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if Cells.cells[start_row + i][start_col + j][2] == num:
                return False
    print('validating: true')
    return True

def solve(row, col, n):
    print('calculating')
    if row == n - 1 and col == n:
        return True

    if col == n:
        row += 1
        col = 0

    if Cells.cells[row][col][2] != 0:
        return solve(row, col + 1, n)

    for i in range(1, n + 1, 1):
        if is_valid(row, col, i, n):
            Cells.cells[row][col][2] = i
            num_surf = Cells.cell_font.render(str(i), True, 'blue')
            num_rect = num_surf.get_rect(center=(Cells.cells[row][col][0] + cell_size // 2, Cells.cells[row][col][1] + cell_size // 2))
            Cells.cells[row][col][3] = num_surf
            Cells.cells[row][col][4] = num_rect
            print(f'{row}, {col}: {Cells.cells[row][col]}')
            if solve(row, col + 1, n):
                return True

        Cells.cells[row][col][2] = 0

    return False