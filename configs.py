WIDTH = 502
HEIGHT = 660
box_size = 162
cell_size = 50

# pads for cells
title_pad = 85
border_pad = 5
small_pad = 3

# pads for number buttons
bottom_pad = 12
LR_pad = 24
mid_pad = 6

# pad for solve reset buttons
x_pad = 24
y_pad = 20
solve_width = 80
solve_height = 40

button_width = 40
button_height = 60

grid_start = [border_pad+small_pad, title_pad+small_pad]
grid_end = [grid_start[0] + small_pad*12 + cell_size*9, grid_start[1] + small_pad*12 + cell_size*9]

is_solved = False