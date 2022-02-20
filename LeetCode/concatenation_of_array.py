# https://leetcode.com/problems/concatenation-of-array/
from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums


if __name__ == '__main__':
    solution = Solution()
    print(solution.getConcatenation([1, 2, 1]))
