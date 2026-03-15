# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# from ..Graph import Graph

# def brute(mat:list[list[int]],m:int,n:int)->list[list[int]]:

#     # construct the graph from mat
#     g = Graph()
#     pacific_node = m*n
#     atlantic_node = m*n + 1
#     for i in range(m):

#         for j in range(n):

#             node = i*n + j

#             if(i>0 and mat[i-1][j]<=mat[i][j]):
#                 up = (i-1)*n + j
#                 g.add_directed_edge(node,up)
#             if(i<m-1 and mat[i+1][j]<=mat[i][j]):
#                 bottom = (i+1)*n + j
#                 g.add_directed_edge(node,bottom)
#             if(j>0 and mat[i][j-1]<=mat[i][j]):
#                 left = i*n + (j-1)
#                 g.add_directed_edge(node,left)
#             if(j<n-1 and mat[i][j+1]<=mat[i][j]):
#                 right = i*n + (j+1)
#                 g.add_directed_edge(node,right)
            
#             if(j==0 or i==0):
#                 g.add_directed_edge(node,pacific_node)
            
#             if(j==n-1 or i==m-1):
#                 g.add_directed_edge(node,atlantic_node)
    
#     # now for each i,j cell in mat
#     # run a bfs and see if we can reach both atlantic_node and pacific_node
#     # if yes, add (i,j) to the ans list
#     # but it's not optimal
#     pass


def optimal(heights:list[list[int]])->list[list[int]]:

    # flip the question
    # instead of asking can we reach to ocean from (i,j)
    # ask can (i,j) be reached from the ocean?
    # since we know all the border cells are reachable from ocean
    # we only run dfs from those cells

    if not heights:
        return []
    
    m = len(heights)
    n = len(heights[0])

    pacific = set()
    atlantic = set()

    def dfs(r:int,c:int,visited:set):

        visited.add((r,c))

        directions = [(-1,0),(0,-1),(1,0),(0,1)]

        for dr,dc in directions:

            nr,nc = r + dr,c + dc

            if 0<= nr < m and 0<=nc<n and heights[r][c]<=heights[nr][nc] and (nr,nc) not in visited:
                dfs(nr,nc,visited)
        
    # we know that leftmost cells -> reachable from pacific
    # rightmost cells -> reachable from atlantic

    for i in range(m):
        dfs(i,0,pacific)
        dfs(i,n-1,atlantic)
    
    # top cells -> pacific
    # bottom cells -> atlantic
    for j in range(n):
        dfs(0,j,pacific)
        dfs(m-1,j,atlantic)
    
    ans = []

    for i in range(m):
        for j in range(n):
            if (i,j) in pacific and (i,j) in atlantic:
                ans.append([i,j])
    
    return ans


heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

print(optimal(heights))
