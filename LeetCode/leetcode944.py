# https://leetcode.com/problems/delete-columns-to-make-sorted/


from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        grid = ["" for _ in range(n)]

        for i in range(n):
            for text in strs:
                grid[i] = grid[i] + text[i]

        count = 0

        for text in grid:
            text = list(text)

            if text != sorted(text):
                count += 1

        return count


if __name__ == '__main__':
    solution = Solution()
    # print(solution.minDeletionSize(["cba", "daf", "ghi"]))
    print(solution.minDeletionSize(["a", "b"]))
