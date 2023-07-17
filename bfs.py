from collections import deque

def BFS(adj, visited, s, v):
    queue = deque([s])
    visited[s] = True

    while queue:
        curr = queue.popleft()
        v.append(curr)

        for it in adj[curr]:
            if not visited[it]:
                queue.append(it)
                visited[it] = True

def breadthFirstSearch(V, E, edges):
    adj = [[] for _ in range(V)]

    for i in range(E):
        u, v = edges[i]
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * (V + 1)
    vv = []

    for j in range(V):
        if not visited[j]:
            v = []
            BFS(adj, visited, j, v)
            vv.append(v)

    return vv
