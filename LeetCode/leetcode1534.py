from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        result = 0

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i < j < k and abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(
                            arr[i] - arr[k]) <= c:
                        result += 1
        return result
