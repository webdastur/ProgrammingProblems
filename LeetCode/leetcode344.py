# https://leetcode.com/problems/reverse-string/

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)

        for i in range(n):
            item = s.pop()
            s.insert(i, item)


if __name__ == '__main__':
    solution = Solution()
    a = ["h", "e", "l", "l", "o"]
    solution.reverseString(a)
    print(a)
