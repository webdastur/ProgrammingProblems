# 479A - Expression
# https://codeforces.com/problemset/problem/479/A

a = int(input())
b = int(input())
c = int(input())

max_value = a + b + c
max_value = max(a * (b + c), max_value)
max_value = max(a * b * c, max_value)
max_value = max((a + b) * c, max_value)

print(max_value)
