# https://leetcode.com/problems/number-of-good-pairs/
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j:
                    if nums[i] == nums[j]:
                        count += 1

        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.numIdenticalPairs([1, 2, 3, 1, 1, 3]))
