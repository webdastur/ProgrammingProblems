# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/


from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        result = []
        start, end = int(s[0:2][1]), int(s[3:5][1])
        letter_start, letter_end = s[0:2][0], s[3:5][0]

        while letter_start <= letter_end:
            for i in range(start, end + 1):
                result.append(f"{letter_start}{i}")
            letter_start = chr(ord(letter_start) + 1)

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.cellsInRange("A1:F1"))
