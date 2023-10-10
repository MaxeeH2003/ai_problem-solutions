graph = {
    'P':['Q','R','S'],
    'Q':['P','R'],
    'R':['P','Q','T'],
    'T':['R'],
    'S':['P']
}
visited = []
queued = []

def bfs(visited,graph,node):
    visited.append(node)
    queued.append(node)

    while queued:
        s = queued.pop(0)
        print(s,end=' ')

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queued.append(neighbour)

bfs(visited,graph,'P')
