def brute(arr:list):
    
    maxp = float('-inf')
    n = len(arr)
    for i in range(n):
        
        prod = arr[i]
        
        for j in range(i+1,n):
            
            prod*=arr[j]
            
            maxp = max(maxp,prod)
            
            if(prod==0):
                break 
            
    return maxp


def optimal(arr:list):
    
    max_prefix,max_suffix = float('-inf'),float('-inf')
    
    prod_prefix,prod_suffix = 1,1
    
    n = len(arr)
    
    for i in range(n):
        
        prod_prefix*= arr[i]
        max_prefix = max(max_prefix,prod_prefix)
        if(prod_prefix==0):
            prod_prefix=1
            
        prod_suffix*=arr[n-i-1]
        max_suffix = max(max_suffix,prod_suffix)
        if(prod_suffix==0):
            prod_suffix=1
            
    return max(max_prefix,max_suffix)

print(brute([-1,2,-3,0,4,-5]))

print(optimal([-1,2,-3,0,4,-5]))