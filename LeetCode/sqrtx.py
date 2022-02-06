# https://leetcode.com/problems/sqrtx/
class Solution:
    def mySqrt(self, x: int) -> int:
        return self.binary_search(0, x, x)

    def binary_search(self, low, high, x):
        if low < high:
            mid = (low + high + 1) // 2
            if mid * mid > x:
                return self.binary_search(low, mid - 1, x)
            else:
                return self.binary_search(mid, high, x)
        return low


if __name__ == '__main__':
    solution = Solution()
    print(solution.mySqrt(8))
