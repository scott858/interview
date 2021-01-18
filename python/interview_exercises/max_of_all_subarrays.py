def rolling_max(data, k):
    stack = []

    for i, d in enumerate(data, 1):
        while len(stack) and d > stack[-1]:
            stack.pop()
        push(stack, k, d)
        if i >= k:
            print('max {}'.format(stack[0]))


def push(stack, k, d):
    if len(stack) == k:
        stack.pop(0)
    stack.append(d)


if __name__ == '__main__':
    data = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    data = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
    rolling_max(data, 4)
