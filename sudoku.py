import pygame as pg

pg.init()

WIDTH = 502
HEIGHT = 660
box_size = 162
cell_size = 50

# pads
title_pad = 85
border_pad = 5
small_pad = 3

grid_start = [border_pad+small_pad, title_pad+small_pad]
grid_end = [grid_start[0] + small_pad*12 + cell_size*9, grid_start[1] + small_pad*12 + cell_size*9]

hl_x = 0
hl_y = 0

def draw_highlight(x, y):
    # create highlight box
    pg.draw.rect(screen, 'crimson', (cells[x][y][0], cells[x][y][1], cell_size, cell_size), 3, 2)

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Sudoku')
clock = pg.time.Clock()

# create name on top
name_font = pg.font.Font('assets/BaiJamjuree-Bold.ttf', 40)
name_surf = name_font.render('SOLVER', True, 'white')
name_rect = name_surf.get_rect(center=(WIDTH // 2, 75 // 2))



# make list of lists of cell's coordinates
cells = []
# create placeholder for real coords
for i in range(9):
    row = []
    for j in range(9):
        cell = [0, 0, 0]
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
                cells[i][j][1] += small_pad*2
            if j == 3 or j == 6:
                cells[i][j][0] += small_pad*2

while True:
    # event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if grid_start[0] < mouse_pos[0] < grid_end[0] and \
                    grid_start[1] < mouse_pos[1] < grid_end[1]:
                for i in range(9):
                    for j in range(9):
                        if cells[j][i][0] < mouse_pos[0] < (cells[j][i][0] + cell_size) and \
                                cells[j][i][1] < mouse_pos[1] < (cells[j][i][1] + cell_size):
                            hl_x = j
                            hl_y = i
                            break

    screen.fill('burlywood')
    # draw boxes
    for i in range(3):
        for j in range(3):
            pg.draw.rect(screen, 'chocolate', (i*(box_size+3)+5, j*(box_size+3)+85, box_size, box_size), 0, 5)

    # draw cells
    for row in cells:
        for cell in row:
            pg.draw.rect(screen, 'white', (cell[0], cell[1], 50, 50), 0, 2)

    # draw name
    screen.blit(name_surf, name_rect)

    # create highlight box
    draw_highlight(hl_x, hl_y)

    pg.display.update()
    clock.tick(60)
