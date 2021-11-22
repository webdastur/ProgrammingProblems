# 580A - Kefa and First Steps
# https://codeforces.com/problemset/problem/580/A

n = int(input())
a = list(map(int, input().split()))

max_subsegment, subsegment = 1, 1

for i in range(1, n):
    if a[i] >= a[i - 1]:
        subsegment += 1
        max_subsegment = max(max_subsegment, subsegment)
    else:
        subsegment = 1

print(max_subsegment)
