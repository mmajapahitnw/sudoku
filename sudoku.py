import pygame as pg

pg.init()

screen = pg.display.set_mode((506, 550))
pg.display.set_caption('Sudoku')
clock = pg.time.Clock()

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

    pg.display.update()
    clock.tick(60)
