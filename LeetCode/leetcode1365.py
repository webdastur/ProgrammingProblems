# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_sorted = sorted(nums)
        return [nums_sorted.index(i) for i in nums]


if __name__ == '__main__':
    solution = Solution()
    print(solution.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
    print(solution.smallerNumbersThanCurrent([6, 5, 4, 8]))
    print(solution.smallerNumbersThanCurrent([7, 7, 7, 7]))
