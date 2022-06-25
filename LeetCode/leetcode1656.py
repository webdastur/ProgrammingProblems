from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.current_index = 0
        self.arr = [""] * n

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1
        self.arr[idKey] = value

        result = []
        if self.arr[self.current_index]:
            while self.arr[self.current_index]:
                result.append(self.arr[self.current_index])
                if self.current_index != self.n - 1:
                    self.current_index += 1
                else:
                    break
        return result


if __name__ == '__main__':
    obj = OrderedStream(5)
    print(obj.insert(3, "ccccc"))
    print(obj.insert(1, "aaaaa"))
    print(obj.insert(2, "bbbbb"))
    print(obj.insert(5, "eeeee"))
    print(obj.insert(4, "ddddd"))
