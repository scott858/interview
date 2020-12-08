from collections import deque

TOWER_HEIGHT = 3
NUM_RODS = 3

rods = []
for i in range(NUM_RODS):
    rod = deque()
    rod.append(TOWER_HEIGHT + 1)
    rods.append(rod)

for i in range(3, 0, -1):
    rods[0].append(i)

for rod in rods:
    print(rod)


def move(rods, to_rod):
    if len(rods) > 1:
        while True:
            for rod_ix, rod in enumerate(rods):
                if len(rod) > 1:
                    other_rods = rods[:rod_ix] + rods[rod_ix + 1:]
                    for other_rod in other_rods:
                        this_top = rod[-1]
                        next_top = other_rod[-1]
                        if this_top < next_top:
                            other_rod.append(rod.pop())

                    print(rods)
                    if move(other_rods, to_rod):
                        return True
                    else:
                        # backtrace
                        pass
    elif len(rods[0]) == TOWER_HEIGHT + 1:
        return True


def tower_of_hanoi(rods):
    rod_a = rods[0]
    if len(rods) == 1:
        return

    if n % 2 == 0:
        tower_of_hanoi(n - 1, src, aux, dest)
        tower_of_hanoi(n - 1, aux, dest, src)
    else:
        tower_of_hanoi(n - 1, src, aux, dest)
        tower_of_hanoi(n - 1, aux, dest, src)


if __name__ == '__main__':
    tower_of_hanoi(4, 'A', 'C', 'B')
