# 318A - Even odds
# https://codeforces.com/problemset/problem/318/A

n, k = map(int, input().split())

if k <= (n + 1) // 2:
    print(k * 2 - 1)
else:
    print((k - (n + 1) // 2) * 2)
