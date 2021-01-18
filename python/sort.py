def bubble_sort(data):
    """
    time: O(n^2), best O(n)
    space: O(1)
    :param data:
    :return:
    """
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


def quick_sort(data):
    """
    time: O(n*log(n)), worst O(n^2)
    space: O(n)
    :param data:
    :return:
    """
    data_len = len(data)

    left = []
    right = []
    pivot = []
    if data_len > 0:
        pivot.append(data.pop())
        while data:
            d = data.pop()
            if d < pivot[0]:
                left.append(d)
            else:
                right.append(d)

        left = quick_sort(left)
        right = quick_sort(right)
    return left + pivot + right


def quick_sort_inplace(data, l_ix, r_ix):
    """
    time: O(n*log(n)), worst O(n^2)
    space: O(1)
    :param data:
    :param l_ix:
    :param r_ix:
    :return:
    """
    if l_ix < r_ix:
        pivot_ix = l_ix
        for i in range(l_ix, r_ix):
            if data[i] < data[r_ix]:
                data[i], data[pivot_ix] = data[pivot_ix], data[i]
                pivot_ix += 1

        data[pivot_ix], data[r_ix] = data[r_ix], data[pivot_ix]
        quick_sort_inplace(data, l_ix, pivot_ix-1)
        quick_sort_inplace(data, pivot_ix+1, r_ix)


def merge_sort(data):
    """
    time: O(n*log(n)), worst O(n*log(n))
    space: O(n)
    :param data:
    :return:
    """
    data_len = len(data)

    if data_len > 1:
        half_ix = int(data_len / 2)
        left = data[:half_ix]
        right = data[half_ix:]
        left = merge_sort(left)
        right = merge_sort(right)
        data = merge(left, right)
    return data


def merge(left, right):
    data = []
    while left and right:
        if left[0] < right[0]:
            data.append(left.pop(0))
        else:
            data.append(right.pop(0))

    while left:
        data.append(left.pop(0))

    while right:
        data.append(right.pop(0))
    return data


def selection_sort(data):
    """
    time: O(n^2), best O(n^2)
    space: O(1)
    :param data:
    :return:
    """
    data_len = len(data)

    for i in range(data_len):
        small_ix = i
        for j in range(i, data_len - 1):
            next_ix = j + 1
            if data[small_ix] > data[next_ix]:
                small_ix = next_ix

        data[small_ix], data[i] = data[i], data[small_ix]


def insertion_sort(data):
    """
    time: O(n^2), best O(n)
    space: O(1)
    :param data:
    :return:
    """
    data_len = len(data)

    for i in range(1, data_len):
        j = i
        while data[j] < data[j - 1]:
            data[j], data[j - 1] = data[j - 1], data[j]
            j -= 1


def heap_sort(data, end_ix):
    """
    time: O(n*log(n))
    space: O(1)
    :param data:
    :param end_ix:
    :return:
    """
    if end_ix > 0:
        data[0], data[end_ix] = data[end_ix], data[0]
        heap_step(data, 0, end_ix - 1)
        heap_sort(data, end_ix - 1)


def heapify(data):
    data_len = len(data)
    end_ix = data_len - 1
    last_row_ix = int(data_len / 2) - 1
    for i in range(last_row_ix, -1, -1):
        heap_step(data, i, end_ix)


def heap_step(data, parent_ix, end_ix):
    left_ix = 2 * parent_ix + 1
    right_ix = 2 * parent_ix + 2

    if right_ix <= end_ix:
        if data[parent_ix] < data[right_ix]:
            data[parent_ix], data[right_ix] = data[right_ix], data[parent_ix]
            heap_step(data, right_ix, end_ix)
    if left_ix <= end_ix:
        if data[parent_ix] < data[left_ix]:
            data[parent_ix], data[left_ix] = data[left_ix], data[parent_ix]
            heap_step(data, left_ix, end_ix)


def counting_sort_simple(data):
    """
    time: O(n + k)
    space: O(n + k)
    :param data:
    :return:
    """
    k = 70
    n = len(data)

    cumulative_count = [0] * k
    for d in data:
        cumulative_count[d] += 1

    for i in range(1, k):
        cumulative_count[i] += cumulative_count[i - 1]

    out = [0] * n

    for d in data:
        out[cumulative_count[d] - 1] = d
        cumulative_count[d] -= 1
    print(out)
    return out


def counting_sort_radix(data, base=1, radix_pos=0):
    k = base
    n = len(data)

    cumulative_count = [0] * k
    for d in data:
        i = int(d / (base ** radix_pos)) % base
        cumulative_count[i] += 1

    for i in range(1, k):
        cumulative_count[i] += cumulative_count[i - 1]

    out = [0] * n

    for i in range(len(data) - 1, -1, -1):
        ix = int(data[i] / (base ** radix_pos)) % base
        out[cumulative_count[ix] - 1] = data[i]
        cumulative_count[ix] -= 1

    for i in range(len(data)):
        data[i] = out[i]
    print(data)


def radix_sort(data, base):
    """
    time: O(n*k)
    space: O(n + k)
    :param data:
    :return:
    """
    max_data = max(data)
    m = 0
    while int(max_data / (base ** m)) > 0:
        counting_sort_radix(data, base=base, radix_pos=m)
        m += 1


def bucket_sort(data):
    buckets = [[] for i in range(10)]
    for d in data:
        i = int(d / 10)
        buckets[i].append(d)

    for bucket in buckets:
        insertion_sort(bucket)
    out = []
    for bucket in buckets:
        out += bucket
    print(out)
    return out


def insertion_sort_2(data):
    data_len = len(data)
    for i in range(data_len):
        j = i
        while data[j] < data[j - 1] and j > 0:
            data[j], data[j - 1] = data[j - 1], data[j]
            j -= 1


def shell_sort(data):
    data_len = len(data)
    gap = int(data_len / 2)

    while gap > 0:
        for i in range(gap, data_len):

            j = i
            while data[j] < data[j - gap] and j >= gap:
                data[j], data[j - gap] = data[j - gap], data[j]
                j -= gap

        gap = int(gap / 2)


if __name__ == '__main__':
    data = [1, 1, 1, 4, 2, 67, 9, 34, 5, 40, 39, 38, 7, 6]
