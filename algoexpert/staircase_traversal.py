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


def staircaseTraversal_memoization(height, maxSteps):
    # Write your code here.
    return numberOfWaysToTop_memoized(height, maxSteps, {0: 1, 1: 1})


def numberOfWaysToTop_memoized(height, maxSteps, memoized):
    if height in memoized:
        return memoized[height]
    number_of_ways = 0
    for step in range(1, min(maxSteps, height) + 1):
        number_of_ways += numberOfWaysToTop_memoized(height - step, maxSteps, memoized)

    memoized[height] = number_of_ways

    return number_of_ways