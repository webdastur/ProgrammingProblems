# https://leetcode.com/problems/maximum-subarray/
from typing import List


class Solution:
    # Brute force solution O(n)
    def maxSubArray(self, nums: List[int]) -> int:
        result, s = nums[0], 0

        for i in nums:
            s += i
            result = max(s, result)
            s = s if s > 0 else 0

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
