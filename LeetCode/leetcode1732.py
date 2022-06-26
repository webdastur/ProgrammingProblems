# https://leetcode.com/problems/find-the-highest-altitude/

from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gain.insert(0, 0)

        s = 0

        for i in range(0, len(gain) - 1):
            s += gain[i + 1]
            gain[i + 1] = s

        return max(gain)
