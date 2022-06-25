from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum_odd_length = sum(arr)

        for i in range(0, len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if (j - i + 1) % 2 > 0:
                    sum_odd_length += sum(arr[i:j+1])

        return sum_odd_length


if __name__ == '__main__':
    solution = Solution()
    print(solution.sumOddLengthSubarrays([1, 4, 2, 5, 3]))
