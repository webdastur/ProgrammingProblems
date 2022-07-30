# https://leetcode.com/problems/first-letter-to-appear-twice/


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        table = {}

        for i in s:
            if i in table:
                return i
            else:
                table[i] = i
