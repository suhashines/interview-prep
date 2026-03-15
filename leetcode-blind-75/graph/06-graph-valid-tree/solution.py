from collections import defaultdict

def graph_valid_tree(n:int,edges:list)->bool:

    if(len(edges)!=n-1):
        # a valid tree must have (n-1) edges
        return False
    # now we have to check if the graph is connected or not
    graph = defaultdict(list)

    visited = [0]*n 
    # construct the undirected graph
    for u,v in edges:

        graph[u].append(v)
        graph[v].append(u)
    
    comp = 0
    def dfs(node):

        visited[node] = 1

        for v in graph[node]:

            if visited[v] == 0:
                dfs(v)
        visited[node] = 2
    
    for i in range(n):

        if visited[i] == 0 :
            dfs(i)
            comp += 1
    
    return comp == 1

    
edges = [[0,1],[2,3],[2,4],[3,4]]
n = 5
print(graph_valid_tree(n,edges))
