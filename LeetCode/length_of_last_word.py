# https://leetcode.com/problems/length-of-last-word/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len([item for item in s.split(" ") if item][-1])


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLastWord("luffy is still joyboy"))
    print(solution.lengthOfLastWord("   fly me   to   the moon  "))
