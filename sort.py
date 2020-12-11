def bubble_sort(data):
    dlen = len(data)

    for i in range(dlen - 1, 0, -1):
        for j in range(i):
            # compare elements pairwise and promote winner to higher position
            if data[j] > data[j + 1]:
                data[j + 1], data[j] = data[j], data[j + 1]


def bubble_sort_rec(data, l, r):
    if l < r:
        for i in range(l, r):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]

        bubble_sort_rec(data, l + 1, r)


def partition(data, l_ix, r_ix):
    # choose the element to partition by
    pivot = data[r_ix]

    # move smaller values to left at this index
    fill_ix = l_ix - 1

    # fill the left side of the array with elements smaller than the pivot
    for j in range(l_ix, r_ix):
        if data[j] < pivot:
            fill_ix += 1
            data[fill_ix], data[j] = data[j], data[fill_ix]

    # place pivot at the partition boundary
    data[fill_ix + 1], data[r_ix] = data[r_ix], data[fill_ix + 1]
    return fill_ix + 1


def quick_sort(data, l_ix, r_ix):
    if l_ix < r_ix:
        p_ix = partition(data, l_ix, r_ix)

        # recursively sort partitions without pivot element
        # lower partition
        quick_sort(data, l_ix, p_ix - 1)
        # upper partition
        quick_sort(data, p_ix + 1, r_ix)


def merge_sort(data):
    data_len = len(data)
    if data_len <= 1:
        res = data
    else:
        half_ix = int(data_len / 2)
        l = merge_sort(data[:half_ix])
        r = merge_sort(data[half_ix:])
        res = merge(l, r)

    return res


def merge(d1, d2):
    d = []
    while len(d1) and len(d2):
        if d1[0] < d2[0]:
            d10 = d1.pop(0)
            d.append(d10)
        else:
            d20 = d2.pop(0)
            d.append(d20)

    for elem in d1:
        d.append(elem)
    for elem in d2:
        d.append(elem)

    return d


def selection_sort(data):
    data_len = len(data)

    for i in range(data_len):
        small_ix = i
        for j in range(i, data_len - 1):
            next_ix = j + 1
            if data[small_ix] > data[next_ix]:
                small_ix = next_ix

        data[small_ix], data[i] = data[i], data[small_ix]


def insertion_sort(data):
    data_len = len(data)
    for i in range(1, data_len):
        datum = data[i]
        prev_ix = i - 1
        prev_datum = data[prev_ix]
        while datum < prev_datum and prev_ix >= 0:
            print(data)
            data[prev_ix + 1], data[prev_ix] = data[prev_ix], data[prev_ix + 1]
            prev_ix -= 1
            prev_datum = data[prev_ix]


def heap_sort(data):
    heapify(data)

    for i in range(len(data) - 1, -1, -1):
        data[i], data[0] = data[0], data[i]
        heap_step(data, i, 0)


def heap_step(data, n, root_ix):
    left_child_ix = 2 * root_ix + 1
    right_child_ix = 2 * root_ix + 2

    if right_child_ix < n:
        right_child = data[right_child_ix]

        root = data[root_ix]

        if right_child > root:
            data[right_child_ix], data[root_ix] = data[root_ix], data[right_child_ix]
            heap_step(data, n, right_child_ix)

    if left_child_ix < n:
        left_child = data[left_child_ix]

        root = data[root_ix]

        if left_child > root:
            data[left_child_ix], data[root_ix] = data[root_ix], data[left_child_ix]
            heap_step(data, n, left_child_ix)


def heapify(data):
    for i in range(len(data), -1, -1):
        heap_step(data, len(data), i)


if __name__ == '__main__':
    data = [1, 50, 3, 12, 8, 34, 7, 29]
    heap_sort(data)
    print(data)
