# https://leetcode.com/problems/find-if-path-exists-in-graph/

from collections import deque
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}

        for node1, node2 in edges:
            if node1 not in graph:
                graph[node1] = [node2]
            else:
                graph[node1].append(node2)

            if node2 not in graph:
                graph[node2] = graph[node1]
            else:
                graph[node2].append(node1)

        queue = deque([source])
        visited = set()

        while queue:
            node = queue.popleft()

            if node == destination:
                return True

            if node in visited:
                continue

            visited.add(node)

            for item in graph[node]:
                if item not in queue:
                    queue.append(item)

        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2))
    print(solution.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))
