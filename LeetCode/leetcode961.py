# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/


from collections import Counter
from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        counter = Counter(nums)

        return max(counter, key=counter.get)
