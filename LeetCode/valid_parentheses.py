# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        cache_stack = []

        for i in s:
            if i == '(':
                cache_stack.append(i)
            elif i == '{':
                cache_stack.append(i)
            elif i == '[':
                cache_stack.append(i)
            elif i == ')' and len(cache_stack) != 0 and cache_stack[-1] == '(':
                cache_stack.pop()
            elif i == '}' and len(cache_stack) != 0 and cache_stack[-1] == '{':
                cache_stack.pop()
            elif i == ']' and len(cache_stack) != 0 and cache_stack[-1] == '[':
                cache_stack.pop()
            else:
                return False

        return len(cache_stack) == 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid("]"))
