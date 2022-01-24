# O(nlogn + n) time
# O(n) space

def mergeOverlappingIntervals(intervals):
    intervals.sort()
    idx = 1
    start_idx = 0
    current_interval = [intervals[start_idx][0], intervals[start_idx][1]]
    overlaps = []
    while idx < len(intervals):
        # To capture the intervals
        if current_interval[1] < intervals[idx][0]:
            overlaps.append(current_interval)
            current_interval = intervals[idx]
        elif current_interval[1] >= intervals[idx][0]:
            current_interval[1] = max(intervals[idx][1], current_interval[1])
        idx += 1
    overlaps.append(current_interval)
    return overlaps
