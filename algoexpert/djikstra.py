# O(v^2+e) - time
# O(v) - space

def dijkstrasAlgorithm(start, edges):
    rounds = 0
    # Create adjacency matrix
    adj_matrix = []
    for x in range(len(edges)):
        # if edges[x]:
        adj_matrix.append([float("inf")] * len(edges))

    index = start
    nodes_to_traverse = []
    for edge in edges[index]:
        nodes_to_traverse.append({index: edge})
    if adj_matrix:
        adj_matrix[index][index] = 0
    else:
        return -1

    visited = []
    indexes_to_process_next = []
    start_index = 0

    while (len(nodes_to_traverse)):
        nodes = nodes_to_traverse.pop()
        while (nodes):
            start_index = list(nodes.keys())[0]
            target_index = nodes[start_index][0]
            indexes_to_process_next.append(target_index)
            visited.append(nodes)
            min_val = get_min_value(start_index, adj_matrix)
            current_value = adj_matrix[start_index][target_index]
            final_output = min(nodes[start_index][1] + min_val, current_value)
            adj_matrix[start_index][target_index] = final_output
            if nodes_to_traverse:
                nodes = nodes_to_traverse.pop()
            else:
                break
        # Process the queue
        for _ind in indexes_to_process_next:
            next_edges = edges[_ind]
            for next_edge in next_edges:
                if {_ind: next_edge} not in visited:
                    nodes_to_traverse.append(
                        {_ind: next_edge})

    output = []
    for j in range(len(adj_matrix[0])):
        value = -1 if min([row[j] for row in adj_matrix]) == float("inf") else min([row[j] for row in adj_matrix])
        output.append(value)
    return (output)


def get_min_value(j, array):
    min_val = min([row[j] for row in array])
    return 0 if min_val == float("inf") else min_val