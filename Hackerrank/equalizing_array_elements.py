import sys
from collections import defaultdict


def minOperations(arr, threshold, d):
    cache = defaultdict(lambda: [0, 0])
    arr.sort()
    ans = max(arr)
    for i in arr:
        steps = 0
        while True:
            cache[i][0] += 1
            cache[i][1] += steps
            if threshold <= cache[i][0]:
                ans = min(ans, cache[i][1])
            if 0 == i:
                break
            i //= d
            steps += 1
    return ans


if __name__ == '__main__':
    print(minOperations([64, 30, 25, 33], 2, 2))
