puzzle_start = '004006079000000602056092300078061030509000406020540890007410920105000000840600100'
puzzle = '004006079000000602056092300078061030509000406020540890007410920105000000840600100'
valid_nums = '123456789'

NUM_COL = 9
NUM_ROW = 9


def get_row(row_ix):
    row = []
    for col_ix in range(NUM_COL):
        row.append(get_element(row_ix, col_ix))
    return row


def get_col(col_ix):
    col = []
    for row_ix in range(NUM_ROW):
        col.append(get_element(row_ix, col_ix))
    return col


def check_row(row_ix):
    row = get_row(row_ix)
    row_base = []
    for row_el in row:
        if row_el != '0':
            row_base.append(row_el)
    row_len = len(row_base)
    return len(set(row_base)) == row_len


def check_col(col_ix):
    col = get_col(col_ix)
    col_base = []
    for col_el in col:
        if col_el != '0':
            col_base.append(col_el)
    col_len = len(col_base)
    return len(set(col_base)) == col_len


def get_element(row_ix, col_ix):
    return puzzle[NUM_COL * row_ix + col_ix]


def set_element(row_ix, col_ix, val):
    global puzzle
    temp_puzzle = list(puzzle)
    temp_puzzle[NUM_COL * row_ix + col_ix] = val
    puzzle = ''.join(temp_puzzle)


def transform_browcol(brow_ix, bcol_ix, block_ix):
    sub_col_ix = block_ix % 3
    sub_row_ix = int(block_ix / 3)

    base_row_ix = 3 * brow_ix
    row_ix = base_row_ix + sub_row_ix

    base_col_index = 3 * bcol_ix
    col_ix = base_col_index + sub_col_ix
    return row_ix, col_ix


def set_block_element(brow_ix, bcol_ix, block_ix, val):
    row_ix, col_ix = transform_browcol(brow_ix, bcol_ix, block_ix)
    temp_puzzle = list(puzzle)
    temp_puzzle[9 * row_ix + col_ix] = val
    return ''.join(temp_puzzle)


def zero_block(brow_ix, bcol_ix):
    global puzzle
    for i in range(9):
        puzzle = set_block_element(brow_ix, bcol_ix, i, '0')


def get_block(brow_ix, bcol_ix):
    block = []

    base_row_ix = 3 * brow_ix
    base_col_ix = 3 * bcol_ix
    for i in range(3):
        for j in range(3):
            row_ix = base_row_ix + i
            col_ix = base_col_ix + j
            block.append(get_element(row_ix, col_ix))
    return block


def print_puzzle(pzl):
    formatted_puzzle = ''
    for row_ix in range(NUM_ROW):
        for col_ix in range(NUM_COL):
            formatted_puzzle += pzl[NUM_COL * row_ix + col_ix] + ' '

            i_ = col_ix + 1
            if i_ % 9 == 0:
                formatted_puzzle += '\n'
                j_ = row_ix + 1
                if j_ % 3 == 0:
                    formatted_puzzle += '\n'
            elif i_ % 3 == 0:
                formatted_puzzle += ' '

    print(formatted_puzzle)


def get_block_availability(block):
    indices = []
    for ix, val in enumerate(block):
        if val == '0':
            indices.append(ix)

    values = list(set(valid_nums).difference(block))

    return indices, values


def get_puzzle_availability():
    blocks = []
    for i in range(3):
        for j in range(3):
            # put i,j in blocks
            block_ix = [[i, j]]
            avail = get_block_availability(get_block(i, j))
            block_ix.append(avail[0])

            perm = permute(avail[1])
            block_ix.append([list(x) for x in perm])
            blocks.append(block_ix)
    return blocks


def permute(lst):
    out_lst = []
    lst_len = len(lst)
    if lst_len > 1:
        for i in range(lst_len):
            smaller_lst = lst[:i] + lst[i + 1:]
            res = permute(smaller_lst)
            for r in res:
                out_lst.append(lst[i] + r)
    else:
        out_lst = lst

    return out_lst


def next_step_ok(brow_ix, bcol_ix, ix):
    row_ix, col_ix = transform_browcol(brow_ix, bcol_ix, ix)
    return check_row(row_ix) and check_col(col_ix)


def check_block(brow_ix, bcol_ix):
    base_row_ix = brow_ix * 3
    base_col_ix = bcol_ix * 3
    check_ok = True
    for i in range(3):
        check_ok = check_ok and check_row(base_row_ix + i)
        check_ok = check_ok and check_col(base_col_ix + i)
        if check_ok is False:
            break
    return check_ok


def solve(pa):
    global puzzle
    if len(pa) > 0:
        (brow_ix, bcol_ix), ixs, vals = pa[0]
        for arr in vals:
            perm = zip(ixs, arr)
            for val in perm:
                puzzle = set_block_element(brow_ix, bcol_ix, val[0], val[1])
            print_puzzle(puzzle)
            if check_block(brow_ix, bcol_ix):
                if solve(pa[1:]):
                    return True

        for ix in ixs:
            puzzle = set_block_element(brow_ix, bcol_ix, ix, '0')
        print_puzzle(puzzle)
        return False

    return True


if __name__ == '__main__':
    pa = get_puzzle_availability()

    print(pa)

    print(solve(pa))
    print_puzzle(puzzle)

    # print(check_block(0, 0))

    # set_element(1, 1, '5')
    # print_puzzle(puzzle)
    # print(check_row(0))
    # print(check_col(0))
    # block = get_block(2, 1)
    # print(block)
    #
    # block_indices, block_values = get_block_availability(block)
    # print(block_indices)
    # print(block_values)
    #
    # print(get_puzzle_availability())

    # lst = list(set(valid_nums).difference(block))
    # perms = set(permute(lst))
    # print(perms)
    # print(len(perms))

    # print_puzzle(puzzle)
    #
    # new_pzl = set_block_element(0, 0, 8, '9')
    # print_puzzle(new_pzl)
