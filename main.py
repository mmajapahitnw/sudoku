import pygame as pg
from cells import Cells
from configs import *
from calculate import solve

pg.init()

# highlight box coordinates
hl_x = 0
hl_y = 0

game_solve = False

class NumberButton(pg.sprite.Sprite):
    def __init__(self, index):
        super().__init__()
        self.image = pg.image.load('assets/num_frame.png')
        self.index = index
        self.rect = self.image.get_rect(topleft=(LR_pad + self.index*(button_width+mid_pad),
                                                 HEIGHT-bottom_pad-button_height))

    def button_clicked(self, num):
        Cells.cells[hl_x][hl_y][2] = num
        num_surf = Cells.cell_font.render(str(num), True, 'red')
        num_rect = num_surf.get_rect(center=(Cells.cells[hl_x][hl_y][0]+cell_size//2,
                                             Cells.cells[hl_x][hl_y][1]+cell_size//2))
        Cells.cells[hl_x][hl_y][3] = num_surf
        Cells.cells[hl_x][hl_y][4] = num_rect

    def update(self):
        for button in num_buttons:
            if button.rect.collidepoint(event.pos):
                self.button_clicked(button.index)



def draw_highlight(x, y):
    # create highlight box
    pg.draw.rect(screen, 'crimson', (Cells.cells[x][y][0], Cells.cells[x][y][1], cell_size, cell_size), 3, 2)

def draw_number():
    for i in range(9):
        for j in range(9):
            if Cells.cells[j][i][2] != 0:
                screen.blit(Cells.cells[j][i][3], Cells.cells[j][i][4])

def reset_values():
    for i in range(9):
        for j in range(9):
            Cells.cells[j][i][2] = 0

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Sudoku')
clock = pg.time.Clock()

# create name on top
name_font = pg.font.Font('assets/BaiJamjuree-Bold.ttf', 40)
name_surf = name_font.render('SOLVER', True, 'white')
name_rect = name_surf.get_rect(center=(WIDTH // 2, 75 // 2))

# solve and reset buttons
solve_reset_font = pg.font.Font('assets/BaiJamjuree-Bold.ttf', 20)

solve_surf = pg.image.load('assets/solve_reset_frame.png')
solve_rect = solve_surf.get_rect(topleft=(x_pad, y_pad))
solve_text = solve_reset_font.render('SOLVE', True, 'brown')
solve_text_rect = solve_text.get_rect(center=(x_pad+solve_width//2, y_pad+solve_height//2))

reset_surf = pg.image.load('assets/solve_reset_frame.png')
reset_rect = reset_surf.get_rect(topright=(WIDTH-x_pad, y_pad))
reset_text = solve_reset_font.render('RESET', True, 'brown')
reset_text_rect = reset_text.get_rect(center=((WIDTH-x_pad)-solve_width//2, y_pad+solve_height//2))

# sprites time!
num_buttons = pg.sprite.Group()
num_surfs = []

for i in range(10):
    if i == 0:
        num_surf = name_font.render('X', True, 'black')
    else:
        num_surf = name_font.render(str(i), True, 'black')
    num_buttons.add(NumberButton(i))
    num_rect = num_surf.get_rect(center=(LR_pad + (i)*(button_width+mid_pad) + button_width//2,
                                         HEIGHT-bottom_pad-button_height//2))
    item = [num_surf, num_rect]
    num_surfs.append(item)


############### THE MAIN LOOP ##############
while True:
    if not game_solve:
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
                            if Cells.cells[j][i][0] < mouse_pos[0] < (Cells.cells[j][i][0] + cell_size) and \
                                    Cells.cells[j][i][1] < mouse_pos[1] < (Cells.cells[j][i][1] + cell_size):
                                hl_x = j
                                hl_y = i
                                break
                elif mouse_pos[1] < title_pad:
                    if solve_rect.collidepoint(mouse_pos):
                        is_solved = solve(0, 0, 9)
                        game_solve = True
                    elif reset_rect.collidepoint(mouse_pos):
                        reset_values()
                else:
                    num_buttons.update()

        screen.fill('burlywood')
        # draw boxes
        for i in range(3):
            for j in range(3):
                pg.draw.rect(screen, 'chocolate', (i*(box_size+3)+5, j*(box_size+3)+85, box_size, box_size), 0, 5)

        # draw cells
        for row in Cells.cells:
            for cell in row:
                pg.draw.rect(screen, 'white', (cell[0], cell[1], 50, 50), 0, 2)

        # draw solve and reset buttons
        screen.blit(solve_surf, solve_rect)
        screen.blit(solve_text, solve_text_rect)
        screen.blit(reset_surf, reset_rect)
        screen.blit(reset_text, reset_text_rect)

        # draw num buttons
        num_buttons.draw(screen)

        # draw num on buttons
        for i in range(10):
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
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                if mouse_pos[1] < title_pad:
                    if reset_rect.collidepoint(mouse_pos):
                        reset_values()
                        game_solve = False
        draw_number()

    pg.display.update()
    clock.tick(60)