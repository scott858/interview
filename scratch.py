"""
-- bubble sort
---- optimize by stopping if no swaps
-- insertion sort
-- selection sort
-- quick sort
-- merge sort
-- tim sort
-- heap sort
-- tree sort
-- radix sort
-- bucket sort
-- shell sort
"""


def bubble_sort(data):
    data_len = len(data)
    for i in range(data_len - 1, 0, -1):
        for j in range(i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]


def bubble_sort_rec(data, l, r):
    if l < r:
        for i in range(l, r):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]

        bubble_sort_rec(data, l + 1, r)


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


def quick_sort(data):
    data_len = len(data)

    if data_len > 1:
        l = []
        r = []
        pivot = data.pop()
        for d in data:
            if d <= pivot:
                l.append(d)
            else:
                r.append(d)
        res = quick_sort(l) + [pivot] + quick_sort(r)
    else:
        res = data

    return res


if __name__ == '__main__':
    d = [1, 4, 6, 3, 42, 7, 9, 44, 2]
    res = quick_sort(d)
    print(res)
