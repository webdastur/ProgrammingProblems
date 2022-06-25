from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set([i for i in allowed])
        result = 0

        for word in words:
            satisfied = True
            for letter in word:
                if letter not in allowed_set:
                    satisfied = False
                    break
            if satisfied:
                result += 1

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]))
