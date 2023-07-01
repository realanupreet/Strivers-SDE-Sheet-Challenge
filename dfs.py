def DFS(adj, visited, s, v):
    visited[s] = True

    for it in adj[s]:
        if not visited[it]:
            v.append(it)
            visited[it] = True
            DFS(adj, visited, it, v)

def depthFirstSearch(V, E, edges):
    adj = [[] for _ in range(V)]

    for i in range(E):
        u, v = edges[i]
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * (V + 1)
    vv = []

    for j in range(V):
        if not visited[j]:
            v = [j]
            DFS(adj, visited, j, v)
            vv.append(v)

    return vv
