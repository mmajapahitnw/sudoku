import pygame as pg
from cells import Cells
from configs import *
from calculate import solve, is_valid

pg.init()

# define all of config variables


hl_x = 0
hl_y = 0

game_solve = False



class Number_Button(pg.sprite.Sprite):
    def __init__(self, index):
        super().__init__()
        self.image = pg.image.load('assets/num_frame.png')
        self.index = index
        self.rect = self.image.get_rect(topleft=(LR_pad + self.index*(button_width+mid_pad), HEIGHT-bottom_pad-button_height))

    def button_clicked(self, num):
        Cells.cells[hl_x][hl_y][2] = num
        num_surf = Cells.cell_font.render(str(num), True, 'red')
        num_rect = num_surf.get_rect(center=(Cells.cells[hl_x][hl_y][0]+cell_size//2, Cells.cells[hl_x][hl_y][1]+cell_size//2))
        Cells.cells[hl_x][hl_y][3] = num_surf
        Cells.cells[hl_x][hl_y][4] = num_rect

    def update(self):
        for button in num_buttons:
            if button.rect.collidepoint(event.pos):
                self.button_clicked(button.index+1)



def draw_highlight(x, y):
    # create highlight box
    pg.draw.rect(screen, 'crimson', (Cells.cells[x][y][0], Cells.cells[x][y][1], cell_size, cell_size), 3, 2)

def draw_number():
    for i in range(9):
        for j in range(9):
            if Cells.cells[j][i][2] != 0:
                screen.blit(Cells.cells[j][i][3], Cells.cells[j][i][4])

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Sudoku')
clock = pg.time.Clock()

# create name on top
name_font = pg.font.Font('assets/BaiJamjuree-Bold.ttf', 40)
name_surf = name_font.render('SOLVER', True, 'white')
name_rect = name_surf.get_rect(center=(WIDTH // 2, 75 // 2))

# create font for cells

# cell_printed = []


# make list of lists of cell's coordinates



# sprites time!
num_buttons = pg.sprite.Group()
num_surfs = []

for i in range(1, 10):
    num_buttons.add(Number_Button(i-1))
    num_surf = name_font.render(str(i), True, 'black')
    num_rect = num_surf.get_rect(center=(LR_pad + (i-1)*(button_width+mid_pad) + button_width//2, HEIGHT-bottom_pad-button_height//2))
    item = [num_surf, num_rect]
    num_surfs.append(item)


############### THE MAIN LOOP ##############
while True:
    if not game_solve:
        # event loop
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                print(Cells.cells[0][5][2])
                is_solved = solve(0, 0, 9)
                game_solve = True
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    num_buttons.update()
                mouse_pos = pg.mouse.get_pos()
                if grid_start[0] < mouse_pos[0] < grid_end[0] and \
                        grid_start[1] < mouse_pos[1] < grid_end[1]:
                    for i in range(9):
                        for j in range(9):
                            if Cells.cells[j][i][0] < mouse_pos[0] < (Cells.cells[j][i][0] + cell_size) and \
                                    Cells.cells[j][i][1] < mouse_pos[1] < (Cells.cells[j][i][1] + cell_size):
                                hl_x = j
                                hl_y = i
                                break

        screen.fill('burlywood')
        # draw boxes
        for i in range(3):
            for j in range(3):
                pg.draw.rect(screen, 'chocolate', (i*(box_size+3)+5, j*(box_size+3)+85, box_size, box_size), 0, 5)

        # draw cells
        for row in Cells.cells:
            for cell in row:
                pg.draw.rect(screen, 'white', (cell[0], cell[1], 50, 50), 0, 2)

        # draw num buttons
        num_buttons.draw(screen)

        # draw num on buttons
        for i in range(9):
            screen.blit(num_surfs[i][0], num_surfs[i][1])

        # draw name
        screen.blit(name_surf, name_rect)

        # create highlight box
        draw_highlight(hl_x, hl_y)

        # draw number
        draw_number()

    else:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
        # if is_solved:
        draw_number()


    pg.display.update()
    clock.tick(60)