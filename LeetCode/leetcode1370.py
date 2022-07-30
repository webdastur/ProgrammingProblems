# https://leetcode.com/problems/increasing-decreasing-string/submissions/


from collections import Counter
from string import ascii_lowercase


class Solution:
    def sortString(self, s: str) -> str:
        counter = Counter(s)
        result = []

        while counter.keys():
            for i in ascii_lowercase:
                if i in counter:
                    result.append(i)
                    counter[i] -= 1
                    if counter[i] == 0:
                        del counter[i]
            for i in ascii_lowercase[::-1]:
                if i in counter:
                    result.append(i)
                    counter[i] -= 1
                    if counter[i] == 0:
                        del counter[i]
        return "".join(result)


if __name__ == '__main__':
    solution = Solution()
    print(solution.sortString("aaaabbbbcccc"))
