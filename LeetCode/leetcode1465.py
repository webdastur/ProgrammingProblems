# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        h, w = 0, 0

        for i in range(1, len(horizontalCuts)):
            w = max(w, horizontalCuts[i] - horizontalCuts[i - 1])

        for j in range(1, len(verticalCuts)):
            h = max(h, verticalCuts[j] - verticalCuts[j - 1])

        return (h * w) % (10 ** 9 + 7)
