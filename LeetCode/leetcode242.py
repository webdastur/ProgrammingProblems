# https://leetcode.com/problems/valid-anagram/


from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ts = Counter(s)
        tt = Counter(t)

        for i in ts:
            if i in tt and tt[i] == ts[i]:
                continue
            else:
                return False

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isAnagram('rat', 'car'))
    print(solution.isAnagram('anagram', 'nagaram'))
