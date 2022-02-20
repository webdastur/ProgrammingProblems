# https://leetcode.com/problems/richest-customer-wealth/
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest_customer = 0
        for i in accounts:
            richest_customer = max(sum(i), richest_customer)
        return richest_customer


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumWealth([[1, 5], [7, 3], [3, 5]]))
