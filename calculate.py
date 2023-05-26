def is_valid(cells, row, col, num, n):
    for i in range(n):
        if cells[row][i].get() == num:
            return False

    for i in range(n):
        if cells[i][col].get() == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if cells[start_row + i][start_col + j].get() == num:
                return False

    return True

def solve(cells, row, col, n):
    if row == n - 1 and col == n:
        return True

    if col == n:
        row += 1
        col = 0

    if cells[row][col].get() != "":
        return solve(cells, row, col + 1, n)

    for i in range(1, n + 1, 1):
        if is_valid(cells, row, col, str(i), n):
            cells[row][col].insert(0, str(i))
            cells[row][col].config(fg='yellow')
            # window.update()
            if solve(cells, row, col + 1, n):
                return True

        cells[row][col].delete(0, END)

    return False