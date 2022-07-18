# https://leetcode.com/problems/decode-the-message/submissions/

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key = key.replace(" ", "")
        table = {}

        current_chr = 97

        result = ""

        for i in key:
            if i not in table and i != " ":
                table[i] = chr(current_chr)
                current_chr += 1

        for i in message:
            if i != " ":
                result += table[i]
            else:
                result += i

        return result

