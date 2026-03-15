def optimal(grid:list[list[int]])->int:

    if not grid:
        return 0
    
    m = len(grid)
    n = len(grid[0])

    visited = [[0]*n for _ in range(m)]

    def dfs(r,c):

        visited[r][c] = 1

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for dr,dc in directions:

            nr,nc = r+dr,c+dc

            if 0<=nr<m and 0<=nc<n and grid[nr][nc] =="1" and visited[nr][nc] == 0:
                dfs(nr,nc)
    islands = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1" and visited[i][j]==0 :
                dfs(i,j)
                islands += 1
    
    return islands


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(optimal(grid))

