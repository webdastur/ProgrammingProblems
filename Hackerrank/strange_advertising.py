import math


def viralAdvertising(n: int) -> int:
    cumulative = 0
    shared = 5
    for i in range(1, n + 1):
        shared = math.floor(shared / 2)
        cumulative += shared
        shared *= 3
    return cumulative


print(viralAdvertising(5))
