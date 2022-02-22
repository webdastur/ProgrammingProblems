# https://leetcode.com/problems/decode-xored-array/
from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]

        for i in range(len(encoded)):
            result.append(encoded[i] ^ result[i])

        return result
