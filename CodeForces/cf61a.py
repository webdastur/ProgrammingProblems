# 61A - Ultra-Fast Mathematician
# https://codeforces.com/problemset/problem/61/A

a = input()
b = input()

result = []

for i in range(len(a)):
    if a[i] != b[i]:
        result.append('1')
    else:
        result.append('0')

print(''.join(result))
