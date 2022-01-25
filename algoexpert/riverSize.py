#O(vh) - time, v = vertices, h = height
def riverSizes(matrix):
    adjacency_graph = [[0 for x in y] for y in matrix]
    output = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if adjacency_graph[i][j]:
                continue
            dfs_traversal_from_node(i, j, matrix, adjacency_graph, output)
    return output


def dfs_traversal_from_node(i, j, matrix, adjacency_graph, output):
    river_size = 0
    nodes_to_explore = [[i, j]]
    while len(nodes_to_explore):
        curentNode = nodes_to_explore.pop()
        i = curentNode[0]
        j = curentNode[1]
        if adjacency_graph[i][j]:
            continue
        adjacency_graph[i][j] = 1
        if matrix[i][j] == 0:
            continue
        river_size += 1
        unvisitedNeighbours = getUnvisitedNeighbours(i, j, adjacency_graph, matrix)
        for neighbour in unvisitedNeighbours:
            nodes_to_explore.append(neighbour)
    if river_size > 0:
        output.append(river_size)


def getUnvisitedNeighbours(i, j, adjacency_graph, matrix):
    unvisited_neighbours = []
    if i > 0 and not adjacency_graph[i - 1][j]:
        unvisited_neighbours.append([i - 1, j])
    if i < len(matrix) - 1 and not adjacency_graph[i + 1][j]:
        unvisited_neighbours.append([i + 1, j])
    if j > 0 and not adjacency_graph[i][j - 1]:
        unvisited_neighbours.append([i, j - 1])
    if j < len(matrix[0]) - 1 and not adjacency_graph[i][j + 1]:
        unvisited_neighbours.append([i, j + 1])
    return unvisited_neighbours