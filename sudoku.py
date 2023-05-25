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
        if i == 0 and j == 0:
            x = y = 8
        else:
            if i == 0:
                y = 8
                x = cells[i][j-1][0] + 53
                if j == 3 or j == 6:
                    x += 5
            elif j == 0:
                x = 8
                y = cells[i-1][j][1] + 53
                if i == 3 or i == 6:
                    y += 5
            else:
                x = cells[i - 1][j][0] + 53
                y = cells[i][j - 1][1] + 53
                if i == 3 or i == 6:
                    x += 5
                if j == 3 or j == 6:
                    y += 5
        cell = (x, y)
        row.append(cell)
    cells.append(row)

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

    # for (x, y) in cells:
    #     pg.draw.rect(screen, 'light yellow', (x, y, 50, 50), 0, 2)

    pg.display.update()
    clock.tick(60)
