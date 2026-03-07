def kadane(arr:list):
    
    sum = 0
    maxsum = float('-inf')
    
    n = len(arr)
    
    for i in range(n):
        
        sum += arr[i]
        maxsum = max(maxsum,sum)
        
        if sum<0:
            sum = 0
        
    return maxsum


def brute(arr:list): 
    
    maxsum = float('-inf')
    n = len(arr)
    for i in range(n):
        sum = arr[i]
        for j in range(i+1,n):
            sum = max(sum,sum+arr[j])
        
        maxsum = max(maxsum,sum)
    return maxsum


print(kadane([-2, -3, -7, -2, -10, -4]))

print(brute([-2, -3, -7, -2, -10, -4]))