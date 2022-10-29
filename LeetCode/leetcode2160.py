class Solution:
    def minimumSum(self, num: int) -> int:
        digits = []
        while num // 10 != 0:
            digits.append(num % 10)
            num = num // 10
        digits.append(num)
        digits.sort()
        return (digits[0] * 10 + digits[2]) + (digits[1] * 10 + digits[3])


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumSum(2932))
