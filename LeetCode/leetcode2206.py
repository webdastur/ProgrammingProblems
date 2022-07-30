# https://leetcode.com/problems/divide-array-into-equal-pairs/


from collections import Counter
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        return all(counter[i] % 2 == 0 for i in counter)
