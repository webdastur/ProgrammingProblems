# https://leetcode.com/problems/count-common-words-with-one-occurrence/


from collections import Counter
from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c1 = Counter(words1)
        c2 = Counter(words2)

        count = 0

        for key in c1:
            if c1[key] == 1 and c2.get(key, -1) == 1:
                count += 1

        return count
