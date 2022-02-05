# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(sum([int(a, 2), int(b, 2)]))[2:]


if __name__ == '__main__':
    solution = Solution()
    print(solution.addBinary("11", "1"))
