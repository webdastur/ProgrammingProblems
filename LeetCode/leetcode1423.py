# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        s = w = m_w = 0
        n = len(cardPoints)

        for i in range(n):
            s += cardPoints[i]
            if i < n - k:
                w += cardPoints[i]
                m_w = w
            else:
                w = w + cardPoints[i] - cardPoints[i - n + k]
            m_w = min(m_w, w)

        return s - m_w
