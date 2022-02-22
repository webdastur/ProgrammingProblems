# https://leetcode.com/problems/count-items-matching-a-rule/
from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        for i in items:
            t, c, n = i
            if "type" == ruleKey and t == ruleValue:
                count += 1
            elif "color" == ruleKey and c == ruleValue:
                count += 1
            elif "name" == ruleKey and n == ruleValue:
                count += 1
        return count
