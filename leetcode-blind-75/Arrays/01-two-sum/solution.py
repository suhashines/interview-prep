def better(nums:list,tgt:int):
    
    """
    time complexity O(n)
    space complexity O(n)
    
    """
    
    map = {}
    
    for i in range(len(nums)):
        
        x = tgt - nums[i]
        
        if x in map:
            
            return [i,map[x]]
        
        map[nums[i]]=i
    
    return [-1,-1]

def optimal(nums:list,tgt:int):
    
    """
    the optimal solution expects a sorted array
    
    time complexity O(n)
    space complexity O(1)
    """
    
    l,r = 0,len(nums)-1 
    
    while(l!=r):
        
        if(nums[l]+nums[r]==tgt):
            return [l,r]
        
        elif(nums[l]+nums[r]<tgt):
            l+=1
            
        else:
            r-=1
            
    return [-1,-1]
    
    pass


print(better([2,6,2,8,11],4))

print(optimal([2,6,5,8,11],14))