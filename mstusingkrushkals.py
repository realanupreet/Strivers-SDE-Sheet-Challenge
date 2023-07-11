def spanningTree(self, V, adj):
    #code here
    key=[float('inf')]*V
    mst=[False]*V
    parent=[-1]*V
    key[0]=0
    parent[0]=-1
    for i in range(V):
        mini=float('inf')
        u=0
        for v in range(V):
            if mst[v]==False and key[v]<mini:
                u=v
                mini=key[v]
                
        mst[u]=True
        for neighbor, weight in adj[u]:
            v= neighbor
            w=weight
            if mst[v]==False and w<key[v]:
                parent[v]=u
                key[v]=w
    # print(key)
    return sum(key)