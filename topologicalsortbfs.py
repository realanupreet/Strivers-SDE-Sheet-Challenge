class Solution:
    
    #Function to return a list containing vertices in Topological order.
    def __dfsHelper(self, sv, visited, adj, stack):
        visited[sv] = True
        for v in adj[sv]:
            if visited[v] == False:
                self.__dfsHelper(v, visited, adj, stack)
        stack.append(sv)
        
    def dfs(self, V, adj):
        stack = []
        visited = [False for _ in range(V)]
        for i in range(V):
            if visited[i] == False:
                self.__dfsHelper(i, visited, adj, stack)
        return stack
        
    def topoSort(self, V, adj):
        # Code here
        stack = self.dfs(V, adj) 
        return stack[::-1]