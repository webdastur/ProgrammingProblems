# https://leetcode.com/problems/build-array-from-permutation/
from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = nums.copy()
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.buildArray([5, 0, 1, 2, 3, 4]))
