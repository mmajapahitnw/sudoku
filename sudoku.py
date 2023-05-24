import pygame as pg

pg.init()

screen = pg.display.set_mode((500, 550))
pg.display.set_caption('Sudoku')

clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()


    screen.fill((192,96,69))

    pg.display.update()
    clock.tick(60)
