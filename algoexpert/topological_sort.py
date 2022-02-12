def topologicalSort(jobs, deps):
    if jobs is not None:
        visited = []
        top_sort_stack = []
        adj_graph = get_empty_adjacency_graph(jobs)
        adj_graph = populate_in_degree_out_degree(adj_graph, deps)
        edges = create_edges_data_structure_for_cycle_validation(adj_graph)
        if cycleInGraph(edges):
            return []
        node_with_zero_in_degrees = get_node_with_zero_in_degrees(adj_graph, jobs, visited)
        for node in node_with_zero_in_degrees:
            DFS_traversal(node, adj_graph, visited, top_sort_stack, jobs)
        return (list(reversed(top_sort_stack)))

    else:
        return []


def get_empty_adjacency_graph(jobs: list):
    return [[0 for x in range(len(jobs) + 1)] for y in range(len(jobs) + 1)]


def populate_in_degree_out_degree(adj_graph: list, deps: list):
    for edge in deps:
        adj_graph[edge[0]][edge[1]] = 1
    return adj_graph


# O(v) - number of jobs - time
def get_node_with_zero_in_degrees(adj_graph: list, jobs: list, visited: list):
    in_degrees = [0] * (len(jobs) + 1)
    index = 0
    while index < len(jobs) + 1:
        in_count = 0
        for row in adj_graph:
            in_count += row[index]
        in_degrees[index] = in_count
        index += 1
    nodes_with_in_degrees_zero = []
    for job in jobs:
        if in_degrees[job] == 0 and job not in visited:
            nodes_with_in_degrees_zero.append(job)
    return nodes_with_in_degrees_zero


# O(v+e) - number of vertices + no of edges
def DFS_traversal(node, adj_graph, visited, top_sort_stack, jobs):
    if node in visited:
        return True
    if sum(adj_graph[node]) == 0:
        visited.append(node)
        top_sort_stack.append(node)
        return True
    else:
        for next_node, value in enumerate(adj_graph[node]):
            if value == 1 and next_node in jobs:
                DFS_traversal(next_node, adj_graph, visited, top_sort_stack, jobs)
            if value == 1 and next_node not in visited:
                visited.append(next_node)
        top_sort_stack.append(node)


def create_edges_data_structure_for_cycle_validation(adj_graph):
    edges = []
    for index, node in enumerate(adj_graph):
        j_index_list = []
        if sum(node) != 0:
            for j_index, j_val in enumerate(node):
                if j_val == 1:
                    j_index_list.append(j_index)
        edges.append(j_index_list)
    return edges


def cycleInGraph(edges):
    black_bucket = [x for x in range(len(edges))]
    in_progress_bucket = []
    full_visited_bucket = []
    edge = 0
    cycles = []
    while edge < len(edges):
        if edge not in full_visited_bucket and edge not in in_progress_bucket:
            in_progress_bucket.append(edge)
            black_bucket[edge] = None
            get_neighbours(edge, black_bucket, in_progress_bucket, full_visited_bucket, edges, cycles)
            if cycles:
                return True
        edge += 1
    return False


def get_neighbours(edge, black_bucket, in_progress_bucket, full_visited_bucket, edges, cycles):
    children = edges[edge]
    if children is None or children == []:
        in_progress_bucket.remove(edge)
        full_visited_bucket.append(edge)
        return
    else:
        for child in children:
            if child in full_visited_bucket:
                pass
            else:
                if child in in_progress_bucket:
                    cycles.append(child)
                    return
                black_bucket[child] = None
                in_progress_bucket.append(child)
                get_neighbours(child, black_bucket, in_progress_bucket, full_visited_bucket, edges, cycles)
        in_progress_bucket.remove(edge)







