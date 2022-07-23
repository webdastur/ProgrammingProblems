from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        last = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= last:
                operations += last - nums[i] + 1
                last += 1
            else:
                last = nums[i]
        return operations


if __name__ == '__main__':
    solution = Solution()
    print(solution.minOperations([1, 1, 1]))
