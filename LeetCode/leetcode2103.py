# https://leetcode.com/problems/rings-and-rods/submissions/


class Solution:
    def countPoints(self, rings: str) -> int:
        table = {}

        for i in range(0, len(rings), 2):
            if rings[i + 1] in table:
                table[rings[i + 1]] += rings[i]
            else:
                table[rings[i + 1]] = rings[i]
        count = 0
        for i in table:
            if 'R' in table[i] and 'G' in table[i] and 'B' in table[i]:
                count += 1
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.countPoints("B0B6G0R6R0R6G9"))
