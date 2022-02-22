# https://leetcode.com/problems/decompress-run-length-encoded-list/
from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(1, len(nums), 2):
            result.extend([nums[i] for _ in range(nums[i - 1])])
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.decompressRLElist([1, 2, 3, 4]))
    print(solution.decompressRLElist([1, 1, 2, 3]))
