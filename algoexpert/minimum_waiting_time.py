#O(nlogn) time
#O(n) space
def minimumWaitingTime(queries):
    queries.sort()
    waiting_time = 0
    prev_query_waiting_time = 0
    for num in range(len(queries)-1):
        prev_query_waiting_time += queries[num]
        waiting_time = waiting_time + prev_query_waiting_time
    return waiting_time
