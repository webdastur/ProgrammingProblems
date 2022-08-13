# https://leetcode.com/problems/merge-similar-items/

from typing import List


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        table = dict()

        self.calculate(table, items1)
        self.calculate(table, items2)

        result = []

        for value, weight in table.items():
            result.append([value, weight])

        result.sort(key=lambda t: t[0])

        return result

    def calculate(self, table: dict, items: List[List[int]]):
        for item in items:
            if item[0] not in table:
                table[item[0]] = item[1]
            else:
                table[item[0]] += item[1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.mergeSimilarItems([[1, 1], [4, 5], [3, 8]], [[3, 1], [1, 5]]))
