def next_greatest(data):
    data_len = len(data)
    print(data)
    stack = []

    stack.append((0, data[0]))

    greatest_hits = [-1] * data_len

    for i in range(1, data_len):
        test_greater = data[i]
        while len(stack) and stack[-1][1] < test_greater:
            ix, lesser = stack.pop()
            greatest_hits[ix] = test_greater
        stack.append((i, test_greater))

    return greatest_hits
