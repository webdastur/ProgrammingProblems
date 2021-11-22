# 705A - Hulk
# https://codeforces.com/problemset/problem/705/A

n = int(input())

feelings = []

is_hated = True

for i in range(n):
    if is_hated:
        feelings.append('I hate that')
    else:
        feelings.append('I love that')
    is_hated = not is_hated

print(' '.join(feelings)[:-len('that')] + 'it')
