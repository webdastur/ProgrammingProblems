# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1

        if not nums:
            return 0

        if len(nums) == 1:
            return 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[index] = nums[i]
                index += 1

        return index


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicates([1,1]))
    print(solution.removeDuplicates([1]))
    print(solution.removeDuplicates([1, 1, 2]))
    print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
