from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min([len(i) for i in strs])
        prefix = ""

        for i in range(min_len):
            for j in range(len(strs)):
                if strs[j][i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]

        return prefix


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
