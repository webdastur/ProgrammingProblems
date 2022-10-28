# https://leetcode.com/problems/group-anagrams/

from collections import Counter, defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            groups[frozenset(Counter(s).items())].append(s)
        return groups.values()


if __name__ == '__main__':
    solution = Solution()
    print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
