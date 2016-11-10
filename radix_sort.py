
import itertools

numbers = [3,53,12,15,90,12,1,0,10]
RADIX_BASE=10
RADIX_BASE_DIGITS = []


def radix_sort(numbers):
    if not numbers:
        return []

    # Get the maximum digits of the max number in the list
    max_digits = len([x for x in str(max(numbers))])
    for x in range(max_digits+1):
        RADIX_BASE_DIGITS.append(10**x)

    iterations = 0
    while iterations < max_digits:
        bucket_map = [[] for x in range(RADIX_BASE)]
        for number in numbers:
            bucket_map[int(number/RADIX_BASE_DIGITS[iterations])%int(RADIX_BASE)].append(number)
        numbers = list(itertools.chain.from_iterable(bucket_map))
        iterations += 1

    return list(itertools.chain.from_iterable(bucket_map))

if __name__ == "__main__":
    numbers = [10,1,2,3,4,100,23,0,1,11,23,45,67,8,9,34]
    print(radix_sort(numbers))