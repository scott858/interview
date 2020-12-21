def graph_dfs(graph, start_vertex, visited):
    visited.add(start_vertex)
    print(start_vertex, end=' ')
    vertices = graph[start_vertex]
    for next_vertex in vertices:
        if next_vertex not in visited:
            graph_dfs(graph, next_vertex, visited)


def graph_bfs(graph, start_vertex):
    visited = set()
    queue = [start_vertex]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')
            for new_vertex in graph[vertex]:
                queue.append(new_vertex)


def find_all_paths(graph, start, end, path=None, paths=None):
    if path is None:
        path = [start]
    if paths is None:
        paths = []
    for vertex in graph[start]:
        if vertex not in path:
            path.append(vertex)
            if vertex == end:
                paths.append(path.copy())
            else:
                find_all_paths(graph, vertex, end, path, paths)
            # backtrack
            path.pop()
    return paths


def find_shortest_path(graph, start, end):
    queue = [start]
    queued = []
    paths = []
    while queue:
        vertex = queue.pop(0)
        for new_vertex in graph[vertex]:
            if new_vertex not in queued:
                queued.append(new_vertex)
                queue.append(new_vertex)
                paths.append([vertex, new_vertex])
                if new_vertex == end:
                    return paths


if __name__ == '__main__':
    graph = {
        'A': {'B', 'C'},
        'B': {'C', 'D'},
        'C': {'D'},
        'D': {'C', 'E'},
        'E': {'F'},
        'F': {'C'},
    }
    # graph_dfs(graph, 'A', set())
    graph_bfs(graph, 'A')
