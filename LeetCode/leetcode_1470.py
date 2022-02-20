# https://leetcode.com/problems/shuffle-the-array/
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []

        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.shuffle([2, 5, 1, 3, 4, 7], 3))
