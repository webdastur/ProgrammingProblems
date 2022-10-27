# https://leetcode.com/problems/unique-number-of-occurrences/description/

from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        counts = counter.values()
        unique_counts = set(counts)
        return len(counts) == len(unique_counts)


if __name__ == '__main__':
    solution = Solution()
    print(solution.uniqueOccurrences([1, 2, 2, 1, 1, 3]))
    print(solution.uniqueOccurrences([1, 2]))
