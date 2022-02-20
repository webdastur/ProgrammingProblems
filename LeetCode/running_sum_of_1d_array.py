# https://leetcode.com/problems/running-sum-of-1d-array/
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if n == 1:
            return nums

        for i in range(1, n):
            nums[i] += nums[i - 1]

        return nums


if __name__ == '__main__':
    solution = Solution()
    print(solution.runningSum([1, 2, 3, 4]))
