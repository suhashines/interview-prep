def tabulation(arr:list)->int:
    
    n = len(arr)
    
    prev2, prev1 = 0,0
    
    for i in range(n):
        
        curr = max(arr[i]+prev2,prev1)
        prev1,prev2 = curr,prev1
    
    return prev1

arr = [1, 2, 4]
print(tabulation(arr))