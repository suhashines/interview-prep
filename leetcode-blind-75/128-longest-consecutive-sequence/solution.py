def brute_force(nums:list):
    
    nums.sort()
    
    maxlen = 1
    
    if(len(nums)==0):
        maxlen=0
    
    s = 0 
    
    for i in range(1,len(nums)):
        
        if(nums[i]!=nums[i-1]+1):
            maxlen=max(maxlen,i-s)
            s = i
    
    maxlen = max(maxlen,len(nums)-s)
    
    return maxlen


def optimal(nums:list):
    
    s = set(nums)
    
    maxlen = 0
    
    for x in s:
        
        cnt = 1
        
        if x-1 not in s:
            
            # we have a starting of a seq
            while(x+cnt in s):
                cnt+=1
            maxlen = max(maxlen,cnt)
    
    return maxlen 


print(brute_force([1,2,3,5,6,7,8]))

print(optimal([0,3,7,2,5,8,4,6,0,1]))