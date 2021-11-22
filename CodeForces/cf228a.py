# 228A - Is your horseshoe on the other hoof?
# https://codeforces.com/problemset/problem/228/A

s = list(map(int, input().split()))

print(len(s) - len(set(s)))
