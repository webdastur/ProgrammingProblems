# https://leetcode.com/problems/plus-one/
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tens, ones = 0, 0
        for i in range(1, len(digits) + 1):
            last_item = digits[-i]
            last_item += tens
            if i == 1:
                last_item += 1
            tens = last_item // 10
            ones = last_item % 10
            digits[-i] = ones
        # if ones is equal to 0 that means tens is exists
        if ones == 0:
            digits.insert(0, tens)

        return digits


if __name__ == '__main__':
    solution = Solution()
    print(solution.plusOne([4, 3, 2, 1]))
    print(solution.plusOne([9]))
