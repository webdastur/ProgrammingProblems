# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/


from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = Counter(s)

        return all(counter[s[0]] == counter[i] for i in counter)
