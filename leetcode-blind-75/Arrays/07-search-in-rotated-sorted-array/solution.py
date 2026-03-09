def optimal(arr:list,l:int,h:int,target:int):
    
    m = (l+h)//2
    
    if(arr[m]==target): return m
    
    if(l==h): return -1
    
    # now we have to figure out which side of the array is sorted
    
    if(arr[l]<=arr[m]):
        # left side is sorted

        if(target>=arr[l] and target<arr[m]): 
            
            return optimal(arr,l,m-1,target)
        else: 
            
            return optimal(arr,m+1,h,target)
    else:
        # right side is sorted
        
        if(target>arr[m] and target<=arr[h]):
             
            return optimal(arr,m+1,h,target)
        else: 
            
            return optimal(arr,l,m-1,target)
    

def find(arr:list,target:int):
    
    return optimal(arr,0,len(arr)-1,target)

print(find([4,5,6,7,0,1,2],target=2))