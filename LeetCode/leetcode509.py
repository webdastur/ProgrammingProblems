# https://leetcode.com/problems/fibonacci-number/

from functools import cache


class Solution:
    @cache
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)
