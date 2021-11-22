# 405A - Gravity Flip
# https://codeforces.com/problemset/problem/405/A

n = int(input())
a = list(map(int, input().split()))

a.sort()

print(' '.join(str(x) for x in a))
