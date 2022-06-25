from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # a = 97
        # b = 122
        codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        converted_words = set()

        for word in words:
            converted_word = ""

            for letter in word:
                converted_word += codes[ord(letter) - 97]

            converted_words.add(converted_word)

        return len(converted_words)


if __name__ == '__main__':
    solution = Solution()
    print(solution.uniqueMorseRepresentations(["rwjje", "aittjje", "auyyn", "lqtktn", "lmjwn"]))
