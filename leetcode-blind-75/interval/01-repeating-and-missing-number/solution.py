def optimal(arr:list):

    n = len(arr)
    ideal_sum = n*(n+1)//2
    ideal_squared_sum = n*(n+1)*(2*n+1)//6

    # missing -> a
    # duplicate -> b
    sum = 0
    sum_squared = 0
    for i in range(n): 
        sum += arr[i]
        sum_squared += arr[i]*arr[i]
    
    y1 = sum - ideal_sum

    y2 = (sum_squared - ideal_squared_sum)//y1

    b = (y1+y2)//2

    a = (y2-y1)//2

    return [b,a]



nums = [1, 2, 3, 6, 7, 5, 7] 

print(optimal(nums))