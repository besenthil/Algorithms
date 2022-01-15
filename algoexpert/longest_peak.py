# O(n) - time | O(n) - space
def longestPeak(array):
    peaks = []
    idx = 1
    while idx <= len(array) - 2:
        if array[idx] > array[idx - 1] and array[idx] > array[idx + 1]:
            peaks.append(idx)
        idx += 1
    current_longest_peak = 0
    for peak in peaks:
        left_valley = peak
        right_valley = peak
        while left_valley > 0 and array[left_valley] > array[left_valley - 1]:
            left_valley -= 1
        while right_valley <= len(array) - 2 and array[right_valley] > array[right_valley + 1]:
            right_valley += 1
        longest_peak = (right_valley + 1) - left_valley
        if current_longest_peak < longest_peak:
            current_longest_peak = longest_peak
    return current_longest_peak
