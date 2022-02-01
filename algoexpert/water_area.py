# O(n) - time
# O(n) - space
def waterArea(heights):
    if not heights:
        return 0
    min_water_level = [0] * len(heights)
    min_water_level[0] = heights[0]
    idx = 1
    while idx < len(heights):
        if heights[idx] > 0:
            min_water_level[idx] = max(min_water_level[idx - 1], heights[idx])
        else:
            min_water_level[idx] = min_water_level[idx - 1]
        idx += 1
    max_water_level = [0] * len(heights)
    heights.reverse()
    max_water_level[0] = heights[0]
    idx = 1
    while idx < len(heights):
        if heights[idx] > 0:
            max_water_level[idx] = max(max_water_level[idx - 1], heights[idx])
        else:
            max_water_level[idx] = max_water_level[idx - 1]
        idx += 1
    max_water_level.reverse()
    heights.reverse()
    dots = 0
    for idx, val in enumerate(heights):
        dots += min(min_water_level[idx], max_water_level[idx]) - val
    return dots


