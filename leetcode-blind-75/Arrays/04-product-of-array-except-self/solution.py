def optimal(arr:list):
    
    n = len(arr)
    
    parr = [1]
    sarr = [1]
    
    for i in range(1,n):
        
        parr.append(parr[i-1]*arr[i-1]) 
        
        sarr.append(sarr[i-1]*arr[n-i]) 
    
    ans = []
    
    for i in range(n):
        
        left = parr[i]
        right = sarr[n-1-i]
            
        ans.append(left*right)
        
    return ans
    
    
   
    
print(optimal([4,3]))