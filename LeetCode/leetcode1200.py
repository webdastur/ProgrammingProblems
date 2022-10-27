# https://leetcode.com/problems/minimum-absolute-difference/

from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        data = []
        index = 0
        min_item = None
        min_item_index = None

        for i in range(len(arr) - 1):
            v = abs(arr[i] - arr[i + 1])
            data.append([v, [arr[i], arr[i + 1]]])
            if min_item is None:
                min_item = v
            if min_item > v:
                min_item = v
                min_item_index = index
            index += 1

        return [value[1] for value in data[min_item_index:] if value[0] == min_item]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumAbsDifference([4, 2, 1, 3]))
    print(solution.minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27]))
