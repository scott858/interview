NUM_QUEENS = 4
board = ''.join(NUM_QUEENS ** 2 * ['0'])


def print_board(board):
    printy_board = ''
    for i, is_occupied in enumerate(list(board), 1):
        printy_board += is_occupied + ' '
        if i % NUM_QUEENS == 0:
            printy_board += '\n'
    print(printy_board)


def get_row(row_ix):
    row = ''
    for col_ix in range(NUM_QUEENS):
        row += board[NUM_QUEENS * row_ix + col_ix]
    return row


def get_col(col_ix):
    col = ''
    for row_ix in range(NUM_QUEENS):
        col += board[NUM_QUEENS * row_ix + col_ix]
    return col


def get_element(row_ix, col_ix):
    return board[NUM_QUEENS * row_ix + col_ix]


def set_element(row_ix, col_ix, val):
    global board
    temp_board = list(board)
    temp_board[row_ix * NUM_QUEENS + col_ix] = val
    board = temp_board


def get_conflicts(row_ix, col_ix):
    row = get_row(row_ix)
    col = get_col(col_ix)

    temp_row_ix = row_ix
    temp_col_ix = col_ix

    down_diag = []
    while temp_row_ix and temp_col_ix:
        temp_row_ix -= 1
        temp_col_ix -= 1

    while temp_row_ix < NUM_QUEENS and temp_col_ix < NUM_QUEENS:
        down_diag.append(get_element(temp_row_ix, temp_col_ix))
        temp_row_ix += 1
        temp_col_ix += 1

    down_diag = ''.join(down_diag)

    temp_row_ix = row_ix
    temp_col_ix = col_ix

    up_diag = []
    while temp_row_ix < NUM_QUEENS - 1 and temp_col_ix:
        temp_row_ix += 1
        temp_col_ix -= 1

    while temp_row_ix >= 0 and temp_col_ix < NUM_QUEENS:
        up_diag.append(get_element(temp_row_ix, temp_col_ix))
        temp_row_ix -= 1
        temp_col_ix += 1

    up_diag = ''.join(up_diag)

    return row, col, up_diag, down_diag


def test_position(row_ix, col_ix):
    conflicts = get_conflicts(row_ix, col_ix)
    conflicts = ''.join(conflicts)
    return '1' not in conflicts


def linear_to_grid_pos(ix):
    row_ix = int(ix / NUM_QUEENS)
    col_ix = ix % NUM_QUEENS
    return row_ix, col_ix


sol_boards = set()


def solve(queens):
    global board
    if queens > 0:
        for i, occ in enumerate(board):
            if occ == '0':
                row_ix, col_ix = linear_to_grid_pos(i)
                if test_position(row_ix, col_ix):
                    set_element(row_ix, col_ix, '1')
                    solve(queens - 1)
                    set_element(row_ix, col_ix, '0')
    else:
        str_board = ''.join(board)
        if str_board not in sol_boards:
            sol_boards.add(str_board)


if __name__ == '__main__':
    solve(NUM_QUEENS)
    for sol in sol_boards:
        print_board(sol)
