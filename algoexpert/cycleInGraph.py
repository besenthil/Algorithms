# O(v+e) - time
# O(v) - time

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