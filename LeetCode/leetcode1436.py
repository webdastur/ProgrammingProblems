# https://leetcode.com/problems/destination-city/


from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        table = {}

        for city_a, city_b in paths:
            table[city_a] = city_b
            if city_b not in table:
                table[city_b] = None
        for city in table:
            if table[city] is None:
                return city
