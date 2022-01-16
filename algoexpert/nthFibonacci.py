# O(2^n) - time
def getNthFib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    elif n == 0:
        return 0
    else:
        return getNthFib(n - 2) + getNthFib(n - 1)