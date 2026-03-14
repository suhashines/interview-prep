class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node:Node)->Node:
    
    if not node:
        return None
    
    old_to_new = {}
    
    def dfs(node:Node)->Node:
        
        if node in old_to_new:
            return old_to_new[node]
        
        copy = Node(node.val)
        old_to_new[node] = copy
        
        for nei in node.neighbors:
            
            copy.neighbors.append(dfs(nei))
        return copy
        
      
    return dfs(node)