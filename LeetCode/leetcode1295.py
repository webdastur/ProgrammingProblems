# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/


from functools import cache
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0

        for i in nums:
            if self.get_digits_count(i) % 2 == 0:
                count += 1
        return count

    @cache
    def get_digits_count(self, num):
        count = 1
        while num >= 10:
            num = num // 10
            count += 1
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.findNumbers([100000]))
    # print(solution.findNumbers([12, 345, 2, 6, 7896]))
