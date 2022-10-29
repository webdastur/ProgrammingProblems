from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda value: value[0])
        w = 0

        for i in range(len(points) - 1):
            w = max(abs(points[i][0] - points[i + 1][0]), w)

        return w


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxWidthOfVerticalArea([[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]))
