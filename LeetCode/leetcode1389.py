# https://leetcode.com/problems/create-target-array-in-the-given-order/
from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []

        for i in range(len(index)):
            target.insert(index[i], nums[i])

        return target


if __name__ == '__main__':
    solution = Solution()
    print(solution.createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]))
