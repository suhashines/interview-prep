def word_search(board,word):

    m = len(board)
    n = len(board[0])
    visited = set()

    def dfs(r,c,i):

        if i == len(word):
            return True
        
        if r<0 or r>=m or c<0 or c>=n or (r,c) in visited or board[r][c] != word[i]:
            return False
        
        visited.add((r,c))
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        res = False

        for dr,dc in directions:

            nr,nc = r + dr,c + dc
            
            res |= dfs(nr,nc,i+1)
                
        visited.remove((r,c))
        return res
    
    for r in range(m):
        for c in range(n):
            if dfs(r,c,0):
                return True
    
    return False

board = [["a","a","a"],["A","A","A"],["a","a","a"]]
word = "aAaaaAaaA"
# board = [["A"]]
# word = "A"

print(word_search(board,word))