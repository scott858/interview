def count_islands(grid):
    adj_arr = create_adj_arr(grid)

    m = len(grid)
    n = len(grid[0])
    island_count = 0
    visited = set()
    for i in range(m):
        for j in range(n):
            grid_value = grid[i][j]
            grid_vertex = (i, j)
            if grid_value and grid_vertex not in visited:
                island_count += 1
                queue = [x for x in adj_arr[grid_vertex] if x not in visited]
                while len(queue):
                    vertex = queue.pop(0)
                    if vertex not in visited:
                        visited.add(vertex)
                        print(vertex)
                        for new_vertex in adj_arr[vertex]:
                            if new_vertex not in visited:
                                queue.append(new_vertex)

    print(island_count)


def create_adj_arr(grid):
    m = len(grid)
    n = len(grid[0])
    adj_arr = {}
    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                neighbors = [
                    (i - 1, j),
                    (i - 1, j + 1),
                    (i, j + 1),
                    (i + 1, j + 1),
                    (i + 1, j),
                    (i + 1, j - 1),
                    (i, j - 1),
                    (i - 1, j - 1),
                ]
                vertex = (i, j)
                adj_arr[vertex] = []
                for ii, jj in neighbors:
                    if (ii >= 0) and (ii < m) and (jj >= 0) and (jj < n):
                        if grid[ii][jj]:
                            adj_arr[vertex].append((ii, jj))
    return adj_arr


if __name__ == '__main__':
    grid = [
        [0, 1],
        [1, 0],
        [1, 1],
        [1, 0],
    ]

    grid = [
        [0, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 1, 0],
    ]
    count_islands(grid)
