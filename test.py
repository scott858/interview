out_str = ''
out_fib = 0


def reverse_recurse(in_str):
    global out_str
    if len(in_str) < 1:
        return
    out_str += in_str[-1]
    reverse_recurse(in_str[:-1])


def reverse_iter(in_str):
    out_str = ''
    str_len = len(in_str)
    for i in range(str_len):
        out_str += in_str[str_len - i - 1]
    return out_str


def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fib_recursive(n - 1) + fib_recursive(n - 2)


def factorial_recursive(n):
    if n == 0:
        return 1

    return n * factorial_recursive(n - 1)


if __name__ == '__main__':
    res = factorial_recursive(5)
    print(res)
