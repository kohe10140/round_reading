def validPath(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    if source == destination:
        return True
    edges_ = [[] for i in range(n)]
    for e in edges:
        edges_[e[0]].append(e[1])
        edges_[e[1]].append(e[0])

    visit = [False for i in range(n)]
    visit[source] = True
    queue = [] # queue contains nodes to visit
    queue.append(source)
    while len(queue) != 0:
        node = queue.pop(0)
        for adjacent in edges_[node]:
            if adjacent == destination:
                return True
            if not visit[adjacent]:
                visit[adjacent] = True
                queue.append(adjacent)
    return False

if __name__ == '__main__':
    n = 3
    edges = [[0,1],[1,2],[2,0]]
    source = 0
    destination = 2
    print(validPath(n, edges, source, destination))

    n = 6
    edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
    source = 0
    destination = 5
    print(validPath(n, edges, source, destination))

    n = 6
    edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
    source = 3
    destination = 5
    print(validPath(n, edges, source, destination))