# https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        cache = [0, 0]

        for i in position:
            cache[i % 2] += 1

        return min(cache)


if __name__ == '__main__':
    solution = Solution()
    print(solution.minCostToMoveChips([2, 2, 2, 3, 3]))
