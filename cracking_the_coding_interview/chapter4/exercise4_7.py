from collections import deque, defaultdict

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.inbound = 0
        self.next = []

        
class Solution:
    def __init__(self) -> None:
        pass

    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        order = deque()
        process_next = deque()
        inbound = {i: 0 for i in range(numCourses)}
        for pr in prerequisites:
            inbound[pr[0]] += 0
            inbound[pr[1]] += 1
        for key in inbound.keys():
            if inbound[key] == 0: # key == 1
                process_next.append(key)
        while len(process_next) != 0:
            n = process_next.popleft() # n == 1
            for pr in prerequisites: # インプットがnのノードを探索
                if pr[0] == n: # pr == [0, 1]
                    inbound[pr[1]] -= 1
                    if inbound[pr[1]] == 0:
                        process_next.append(pr[1])
            order.appendleft(n)
        if len(order) > numCourses:
            return []
        if sum(list(inbound.values())) > 0:
            return []
        return list(order)

s = Solution()
numCourses = 2
prerequisites = [[1,0]]
print(s.findOrder(numCourses, prerequisites))

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(s.findOrder(numCourses, prerequisites))

numCourses = 1
prerequisites = []
print(s.findOrder(numCourses, prerequisites))

numCourses = 3
prerequisites = [[1,0]]
print(s.findOrder(numCourses, prerequisites))

numCourses = 2
prerequisites = [[1,0], [0,1]]
print(s.findOrder(numCourses, prerequisites))

numCourses = 4
prerequisites = [[3,0],[0,1]]
print(s.findOrder(numCourses, prerequisites))