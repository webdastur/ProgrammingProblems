# https://leetcode.com/problems/maximum-units-on-a-truck/

from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        total_units = 0

        for nn, nu in boxTypes:
            if nn <= truckSize:
                truckSize -= nn
                total_units += nn * nu
            else:
                total_units += truckSize * nu
                break

        return total_units
