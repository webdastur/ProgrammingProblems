# https://leetcode.com/problems/maximum-number-of-pairs-in-array/


from collections import Counter
from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [0, 1]
        counter = Counter(nums)
        operations = 0
        left_over = 0

        for i in counter:
            if counter[i] > 1:
                operations += (counter[i] // 2)
                counter[i] -= (counter[i] // 2 * 2)

            if counter[i] == 1:
                left_over += 1

        return [operations, left_over]


if __name__ == '__main__':
    solution = Solution()
    print(solution.numberOfPairs([1, 3, 2, 1, 3, 2, 2]))
    print(solution.numberOfPairs([0]))
