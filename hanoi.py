from collections import deque

TOWER_HEIGHT = 5
NUM_RODS = 3

rods = []
for i in range(NUM_RODS):
    rod = deque()
    rod.append(TOWER_HEIGHT + 1)
    rods.append(rod)

for i in range(TOWER_HEIGHT, 0, -1):
    rods[0].append(i)


def transfer(rod_1, rod_2):
    l_1 = len(rod_1)
    l_2 = len(rod_2)

    if l_1 > 1 and l_2 > 1:
        if rod_2[-1] < rod_1[-1]:
            rod_1.append(rod_2.pop())
        else:
            rod_2.append(rod_1.pop())
    elif l_1 > 1:
        rod_2.append(rod_1.pop())
    elif l_2 > 1:
        rod_1.append(rod_2.pop())


def move(rods):
    if len(rods[-1]) == TOWER_HEIGHT + 1:
        print(rods)
    else:
        print(rods)
        transfer(rods[0], rods[1])
        print(rods)
        transfer(rods[0], rods[2])
        print(rods)
        transfer(rods[1], rods[2])
        move(rods)


def move_2(n, src, target, aux):
    if n > 0:
        move_2(n - 1, src, aux, target)

        target.append(src.pop())

        move_2(n - 1, aux, target, src)


if __name__ == '__main__':
    # move(rods)
    src = [1, 2, 3]
    target = []
    aux = []
    print('{0} {1} {2}'.format(src, aux, target))
    move_2(len(src), src, target, aux)
    print('{0} {1} {2}'.format(src, aux, target))
