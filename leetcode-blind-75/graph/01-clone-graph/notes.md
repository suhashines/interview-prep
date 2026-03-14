[Clone graph](https://leetcode.com/problems/clone-graph/)

## Problem Statement
Given a reference of a node in a [connected](https://en.wikipedia.org/wiki/Connected_graph) undirected graph, return a **deep copy** (clone) of the graph. Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

## Solution

- We will use dfs to traverse the graph and create a copy of each node. We will use a hashmap to store the mapping between the original node and the copied node.

**Why do we need a hashmap?**
- The hashmap is used to store the mapping between the original node and the copied node. This is necessary because we need to ensure that we do not create multiple copies of the same node. If we encounter a node that we have already copied, we can simply return the copied node from the hashmap instead of creating a new copy.

```python
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else [] 
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None                 
        # Hashmap to store the mapping between original node and copied node
        visited = {}
        def dfs(node):
            if node in visited:
                return visited[node]        
            # Create a copy of the node
            copy = Node(node.val)
            visited[node] = copy
            # Recursively copy the neighbors
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node)
```