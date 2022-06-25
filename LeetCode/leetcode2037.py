from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        min_moves = 0

        seats.sort()
        students.sort()

        for i in range(len(seats)):
            min_moves += abs(seats[i] - students[i])

        return min_moves