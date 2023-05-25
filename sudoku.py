import pygame as pg

pg.init()

screen = pg.display.set_mode((506, 550))
pg.display.set_caption('Sudoku')
clock = pg.time.Clock()

pg.font.Font('assets/BaiJamjuree-Bold.ttf', 20)
cells = []
x, y = 0, 0

for i in range(9):
    row = []
    for j in range(9):
        cell = [0, 0]
        row.append(cell)
    cells.append(row)


for i in range(9):
    for j in range(9):
        if i == 0 and j == 0:
            cells[i][j][0] = cells[i][j][1] = 8
        else:
            if i == 0:
                cells[i][j][1] = 8
                cells[i][j][0] = cells[i][j - 1][0] + 53
            elif j == 0:
                cells[i][j][0] = 8
                cells[i][j][1] = cells[i - 1][j][1] + 53
            else:
                cells[i][j][0] = cells[i][j - 1][0] + 53
                cells[i][j][1] = cells[i - 1][j][1] + 53
            if i == 3 or i == 6:
                cells[i][j][1] += 8
            if j == 3 or j == 6:
                cells[i][j][0] += 8

print(cells)



box_size = 162

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()




    screen.fill((192,96,69))
    for i in range(3):
        for j in range(3):
            pg.draw.rect(screen, 'white', (i*(box_size+5)+5, j*(box_size+5)+5, box_size, box_size), 0, 5)

    for row in cells:
        for x,y in row:
            pg.draw.rect(screen, 'green', (x, y, 50, 50), 0, 2)

    pg.display.update()
    clock.tick(60)
