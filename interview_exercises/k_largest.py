def run_k_largest(data, k):
    heapify(data)
    last_ix = len(data) - 1
    k_largest(data, k, last_ix)
    print(data[-k:][::-1])


def k_largest(data, k, last_ix):
    if k > 0:
        data[0], data[last_ix] = data[last_ix], data[0]
        heap_step(data, 0, last_ix - 1)
        k_largest(data, k - 1, last_ix - 1)
    else:
        print(data)


def heapify(data):
    data_len = len(data)
    last_ix = data_len - 1

    for i in range(data_len, -1, -1):
        heap_step(data, i, last_ix)


def heap_step(data, node_ix, last_ix):
    left_ix = 2 * node_ix + 1
    right_ix = 2 * node_ix + 2

    if right_ix < last_ix:
        if data[node_ix] < data[right_ix]:
            data[node_ix], data[right_ix] = data[right_ix], data[node_ix]
        heap_step(data, right_ix, last_ix)

    if left_ix < last_ix:
        if data[node_ix] < data[left_ix]:
            data[node_ix], data[left_ix] = data[left_ix], data[node_ix]
        heap_step(data, left_ix, last_ix)


