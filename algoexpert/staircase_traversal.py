def staircaseTraversal(height, maxSteps):
    steps = [x for x in range(1, maxSteps + 1)]
    return staircaseTraversal_helper(height, 0, steps)


def staircaseTraversal_helper(height, current_height, steps):
    if current_height == height:
        return 1
    total_ways = 0
    for step in steps:
        if (current_height + step) <= height:
            total_ways += staircaseTraversal_helper(height, current_height + step, steps)
    return total_ways
