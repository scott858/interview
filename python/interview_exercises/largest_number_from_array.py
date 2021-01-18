def largest_number(arr):
    arr.reverse()
    quick_sort(arr, 0, len(arr) - 1)
    arr = [str(x) for x in arr]
    print(''.join(arr))


def quick_sort(arr, l_ix, r_ix):
    if l_ix < r_ix:
        pivot = arr[r_ix]

        pivot_ix = l_ix
        for i in range(l_ix, r_ix):
            if a_greater_than_b(arr[i], pivot):
                arr[i], arr[pivot_ix] = arr[pivot_ix], arr[i]
                pivot_ix += 1

        arr[pivot_ix], arr[r_ix] = arr[r_ix], arr[pivot_ix]

        quick_sort(arr, l_ix, pivot_ix - 1)
        quick_sort(arr, pivot_ix + 1, r_ix)


def a_greater_than_b(a, b):
    a = str(a)
    b = str(b)

    ab = int(a + b)
    ba = int(b + a)

    return ab > ba


if __name__ == '__main__':
    arr = [3, 30, 34, 5, 9]
    # arr = [54, 546, 548, 60]
    largest_number(arr)
