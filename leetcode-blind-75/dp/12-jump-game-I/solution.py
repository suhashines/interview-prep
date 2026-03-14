def jump_game(arr:list[int])->bool:
    n = len(arr)
    dp = [False]*n
    
    dp[n-1] = True
    
    for i in range(n-2,-1,-1):
        
        jmp = n-1 - i

        if(arr[i]>=jmp):
            dp[i] = True
        else:           
            for j in range(1,arr[i]+1):
                dp[i] = dp[i+j]
                if dp[i]:
                    break
    return dp[0]


def optimal(arr:list[int])->bool:
    # Uses the greedy approach
    
    #Track the maximum reachable index iteratively to determine if the end is accessible.
    
     # from index i, how far can I reach? max_reach variable keep tracks of that
    max_reach = 0
   
    
    for i in range(len(arr)):
        
        # is it possible to reach to index i from 0?
        if(i>max_reach):
            return False
        
        max_reach = max(max_reach, i + arr[i])
        # if from 0, index `i` is accessible then all indices from (i,i+arr[i]) is also accessible
        
    
    return True

arr = [3,2,1,0,4]

print(jump_game(arr))