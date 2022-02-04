# O(nlogn) - time
# O(n) - space

def taskAssignment(k, tasks):
    get_task_duration_indices(tasks)
    tasks.sort()
    durations = []
    for n in range(k):
        durations.append([tasks[n], tasks[len(tasks) - n - 1]])

    task_assignments = []
    for duration in durations:
        task_1 = index[duration[0]].pop()
        task_2 = index[duration[1]].pop()
        task_assignments.append([task_1, task_2])
    return task_assignments


def get_task_duration_indices(tasks):
    index = {}
    for idx, item in enumerate(tasks):
        value = index.get(item, None)
        if value:
            index[item].append(idx)
        else:
            index.setdefault(item, [idx])
    return index