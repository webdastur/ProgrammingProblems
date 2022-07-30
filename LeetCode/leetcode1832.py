# https://leetcode.com/problems/check-if-the-sentence-is-pangram/submissions/


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for i in range(97, 123):
            if chr(i) not in sentence:
                return False
        return True
