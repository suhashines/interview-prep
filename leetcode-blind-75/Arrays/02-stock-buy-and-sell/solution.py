def brute(arr:list):
    
    max_profit = 0
    
    for i in range(len(arr)):
        
        profit = 0
        
        for j in range(i+1,len(arr)):

            profit = max(profit,arr[j]-arr[i])
        
        max_profit = max(max_profit,profit)
    
    return max_profit

def optimal(arr:list):
    
    if(len(arr)==0):
        return (-1,-1,0)
    
    best_bi,best_si,bi,maxp = -1,-1,0,0
    
    for i in range(len(arr)):
        
        p = arr[i]-arr[bi]
        
        if(p>maxp):
            
            maxp = p
            best_bi=bi+1
            best_si=i+1
        
        if(arr[i]<arr[bi]):
            bi = i 
    
    return (best_bi,best_si,maxp)
    
    
     

print(brute([7,6,4,3,1]))


print(optimal([10,2,1,4,5,2,10]))