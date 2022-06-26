# https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        data = {}
        max_side = 0

        for i in rectangles:
            min_side = min(i)
            max_side = max(min_side, max_side)

            if min_side in data:
                data[min_side] += 1
            else:
                data[min_side] = 1
        return data[max_side]
