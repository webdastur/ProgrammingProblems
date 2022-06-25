class SortedSums:
    def __init__(self, size):
        self.size = size
        self.arr = [0] * self.size

    def add(self, x, val):
        if x == 0:
            self.arr[0] += val
            return
        while self.size > x:
            self.arr[x] += val
            x += x & (-x)

    def rank(self, x):
        if 0 > x:
            return 0
        res = self.arr[0]
        while 0 < x:
            res += self.arr[x]
            x &= x - 1
        return res


def sortedSum(a):
    pre = SortedSums(10 ** 6 + 1)
    post = SortedSums(10 ** 6 + 1)
    temp = total = ans = 0
    n = len(a)
    for i in range(n):
        pos = pre.rank(a[i]) + 1

        g = total - post.rank(a[i])
        temp = (temp + pos * a[i] + g) % (10 ** 9 + 7)
        ans = (ans + temp) % (10 ** 9 + 7)
        total += a[i]

        pre.add(a[i], 1)
        post.add(a[i], a[i])
    return ans

if __name__ == '__main__':
    print(sortedSum([9, 5, 8]))
