from typing import List


class SolutionBFS:

    def canReach(self, arr: List[int], start: int) -> bool:
        queue = [start]
        visited = set(queue)
        result = False
        while queue and not result:
            pos = queue.pop(0)
            visited.add(pos)
            if arr[pos] == 0:
                result = True
            else:
                next_pos = pos + arr[pos]
                if next_pos < len(arr) and next_pos not in visited:
                    queue.append(next_pos)
                next_pos = pos - arr[pos]
                if next_pos > -1 and next_pos not in visited:
                    queue.append(next_pos)
        return result


class Solution:

    def dfs(self, arr, pos, visited):
        visited.add(pos)
        result = False
        if arr[pos] == 0:
            result = True
        else:
            next_pos = pos + arr[pos]
            if next_pos < len(arr) and next_pos not in visited:
                result = self.dfs(arr, next_pos, visited)
            if not result:
                next_pos = pos - arr[pos]
                if next_pos > -1 and next_pos not in visited:
                    result = self.dfs(arr, next_pos, visited)
        return result

    def canReach(self, arr: List[int], start: int) -> bool:
        return self.dfs(arr, start, set())
