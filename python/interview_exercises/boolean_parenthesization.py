def boolean_parenthesization(ex):
    """
    can be solved with an nxn table for True and a table for False
    :param ex:
    :return:
    """
    ex = [x for x in ex]
    symbs = ex[0::2]
    ops = ex[1::2]
    print(symbs)
    print(ops)
    print()
    combine_symbols(symbs, ops)


def combine_symbols(symbs, ops, sub_exp=None, visited=None):
    if len(symbs) > 1:
        if sub_exp is None:
            sub_exp = symbs.copy()
            visited = set()
        for i in range(len(symbs) - 1):
            symbol_pair_string = (symbs[i], symbs[i + 1])
            bool_res = evaluate_combination(symbol_pair_string, ops[i])
            new_symbol = symbolize_boolean(bool_res)
            new_symbs = symbs[:i] + [new_symbol] + symbs[i + 2:]
            new_ops = ops[:i] + ops[i + 1:]

            sub_ex_term = '({0}{1}{2})'.format(sub_exp[i], ops[i], sub_exp[i + 1])
            new_sub_exp = sub_exp[:i] + [sub_ex_term] + sub_exp[i + 2:]

            new_sub_exp_tuple = tuple(new_sub_exp)
            if new_sub_exp_tuple not in visited:
                visited.add(new_sub_exp_tuple)
                combine_symbols(new_symbs, new_ops, new_sub_exp, visited)
    else:
        print('{0} = {1}'.format(sub_exp[0][1:-1], symbs[0]))
        print()


def symbolize_boolean(the_bool):
    if the_bool:
        return 'T'
    else:
        return 'F'


def evaluate_combination(symb_pair_string, op_string):
    symbol_pair = parse_symbol_pair_string(symb_pair_string)
    operator = parse_operator_string(op_string)
    return operator(symbol_pair)


def parse_symbol_pair_string(pair):
    left_symbol = parse_symbol_string(pair[0])
    right_symbol = parse_symbol_string(pair[1])
    return left_symbol, right_symbol


def parse_symbol_string(sym_string):
    if sym_string == 'T':
        return True
    elif sym_string == 'F':
        return False
    else:
        return None


def parse_operator_string(op_string):
    if op_string == '&':
        return my_and
    elif op_string == '|':
        return my_or
    elif op_string == '^':
        return my_xor


def my_and(symbol_pair):
    return symbol_pair[0] and symbol_pair[1]


def my_or(symbol_pair):
    return symbol_pair[0] or symbol_pair[1]


def my_xor(symbol_pair):
    return symbol_pair[0] ^ symbol_pair[1]


if __name__ == '__main__':
    ex = 'T|T&F^T'
    ex = 'T^F|F'
    boolean_parenthesization(ex)
