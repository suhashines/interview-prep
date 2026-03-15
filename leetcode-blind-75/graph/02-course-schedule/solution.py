import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Graph import Graph

def canFinish(numCourses,prerequisites):

    g = Graph()

    for u,v in prerequisites:
        g.add_directed_edge(v,u)
    
    visited = {}

    def has_cycle(node):

        # mark the node as grey
        # it means we are exploring its neighbors
        visited[node] = 1

        for nei in g.get_neighbors(node):

            if nei not in visited:

                if has_cycle(nei):
                    return True
            if visited[nei] == 1:
                return True
        
        # mark the node as fully processed
        visited[node] = 2
        
        return False
    
    # the graph might be disconnected

    for i in range(numCourses):
        if i not in visited:
            if has_cycle(i):
                # if there is a cycle, we cannot finish all the courses
                return False
    
    return True



prereq = [[1,0],[2,0],[3,1],[4,1],[4,2],[5,2]]

# prereq = [[1,0],[2,1],[0,2]]

print(canFinish(3,prereq))