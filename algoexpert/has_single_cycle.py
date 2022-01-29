# O(n) - time
# O(n) - space
def hasSingleCycle(array):
    edges = []
    for current_index in range(len(array)):
        edges.append(get_index_in_cycle(current_index, array[current_index], array))
    visited = [0 for x in range(len(array))]
    index = 0
    finished_one_cycle = False
    visited[0] = 1
    while (sum(visited) <= len(array) + 1 and not finished_one_cycle):
        next_edge = edges[index][1]
        if visited[next_edge]:
            finished_one_cycle = True
        else:
            visited[next_edge] = 1
        index = edges[index][1]
    return finished_one_cycle and index == 0 and sum(visited) == len(array)


def get_index_in_cycle(current_index, skips, array):
    return [current_index, (current_index + skips) % len(array)]
