# https://leetcode.com/problems/find-greatest-common-divisor-of-array/


from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_item = max_item = nums[0]

        for i in nums:
            if i > max_item:
                max_item = i
            if i < min_item:
                min_item = i

        return self.gcd(min_item, max_item)

    def gcd(self, a, b):
        if b == 0:
            return abs(a)
        else:
            return self.gcd(b, a % b)
