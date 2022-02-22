# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [extraCandies + i >= max_candies for i in candies]


if __name__ == '__main__':
    solution = Solution()
    print(solution.kidsWithCandies([2, 3, 5, 1, 3], 3))
