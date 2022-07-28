# https://leetcode.com/problems/goal-parser-interpretation/


class Solution:
    def interpret(self, command: str) -> str:
        result = []
        index = 0

        while index < len(command):
            if command[index:index + 1] == "G":
                result.append("G")
                index += 1
                continue
            elif command[index:index + 2] == "()":
                result.append("o")
                index += 2
                continue
            elif command[index:index + 4] == "(al)":
                result.append("al")
                index += 4
                continue

        return "".join(result)


if __name__ == '__main__':
    solution = Solution()
    print(solution.interpret("G()(al)"))
