def remain(m, n):
    if m > n:
        bigger = m
        smaller = n
    else:
        bigger = n
        smaller = m

    p = int(bigger / smaller)

    return bigger - p*smaller



if __name__ == '__main__':

    print(remain(13, 4))
    print(remain(4, 13))
    print(remain(1000, 142))
    print(remain(142, 1000))

