# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        s = s.replace('IV', '_4')
        s = s.replace('IX', '_9')
        s = s.replace('XL', '_40')
        s = s.replace('XC', '_90')
        s = s.replace('CD', '_400')
        s = s.replace('CM', '_900')

        s = s.replace('I', '_1')
        s = s.replace('V', '_5')
        s = s.replace('X', '_10')
        s = s.replace('L', '_50')
        s = s.replace('C', '_100')
        s = s.replace('D', '_500')
        s = s.replace('M', '_1000')

        num = s.split('_')

        return sum([int(i) for i in num if i])


if __name__ == '__main__':
    solution = Solution()
    print(solution.romanToInt("LVIII"))
