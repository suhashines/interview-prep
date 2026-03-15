class Graph:
    def __init__(self):
        self.graph = {}

    def add_undirected_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def add_directed_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)


    def get_neighbors(self, node):
        return self.graph.get(node, [])
    
    def dfs(self,node):

        visited = {}

        def recursive_dfs(node):
            
            visited[node] = 1

            for nei in self.graph[node]:
                if nei not in visited:
                    visited[nei] = 1
                    recursive_dfs(nei)
            
            visited[node] = 2 # black
            # print(node,end=" ")
        recursive_dfs(node)


# let's create a graph and test the DFS
# g = Graph()
# g.add_directed_edge(1, 2)
# g.add_directed_edge(1, 3)
# g.add_directed_edge(2, 4)
# g.add_directed_edge(3, 4)
# g.add_directed_edge(4, 5)
# g.dfs(1)
