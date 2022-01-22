# https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.strStr("hello", "ll"))
    print(solution.strStr("aaaaa", "bba"))
    print(solution.strStr("dadabobo", "bo"))
