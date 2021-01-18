def is_triplet(xyz):
    n = len(xyz)

    xyz = list(set(xyz))

    xyz.sort()
    
    z2 = [x ** 2 for x in xyz]
    x2_plus_y2 = {}

    for i in range(n):
        x2_plus_y2[z2[i]] = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            x2_plus_y2[z2[i] + z2[j]] = 1

    success = False
    for d in z2:
        if x2_plus_y2[d]:
            success = True

    if success:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    xyz = [3, 2, 4, 6, 5]
    xyz = [3, 8, 5]
    is_triplet(xyz)
