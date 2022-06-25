from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for x in range(len(image)):
            image[x].reverse()

            image[x] = list(map(lambda i: abs(i - 1), image[x]))
        return image