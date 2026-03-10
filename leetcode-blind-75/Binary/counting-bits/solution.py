def better(num:int)->list:
    
    """
    time complexity: O(nlogn)
    """
    
    ans = []
    
    for i in range(0,num+1):
        
        cnt = 0 
        j = i
        while(j!=0):
            
            if(j%2==1):
                cnt+=1
            j = j//2
        ans.append(cnt)
        
    return ans


def optimal(num:int)->list:
    ans = [0]*(num+1)
    
    offset = 1
    
    for i in range(1,num+1):
        
        if(i == 2*offset):
            # check if i is a power of 2, i.e. 2,4,6,8,16
            offset = i
            
        ans[i] = 1 + ans[i-offset]
        
    return ans 

print(better(10))

print(optimal(10))