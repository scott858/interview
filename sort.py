def bubble_sort(data):
    dlen = len(data)

    for i in range(dlen - 1, 0, -1):
        for j in range(i):
            # compare elements pairwise and promote winner to higher position
            if data[j] > data[j + 1]:
                data[j + 1], data[j] = data[j], data[j + 1]


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
    if data_len > 1:
        half_ix = int(data_len / 2)

        left = data[:half_ix]
        right = data[half_ix:]

        left = merge_sort(left)
        right = merge_sort(right)

        merged = merge(left, right)
    else:
        merged = data

    return merged


def merge(left, right):
    merged = []

    while len(left) and len(right):
        if left[0] < right[0]:
            merged.append(left[0])
            del left[0]
        else:
            merged.append(right[0])
            del right[0]

    if len(left):
        merged += left
    else:
        merged += right

    return merged


def insertion_sort(data):
    # prett sure this is equivalent to bubble sort
    data_out = []
    for datum in data:
        data_out.append(datum)
        for i in range(len(data_out) - 1):
            if datum > data_out[i]:
                continue
            else:
                data_out[i], data_out[-1] = data_out[-1], data_out[i]

    return data_out


if __name__ == '__main__':
    data = [1, 50, 3, 12, 8]

    print(data)

    # bubble_sort(data)
    # quick_sort(data, 0, len(data)-1)
    # data = merge_sort(data)
    data = insertion_sort(data)

    print(data)
