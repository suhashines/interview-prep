def optimal(arr:list)->int:

    n = len(arr)

    total_xor = n+1
    array_xor = 0
    mask = 0xFFFFFFFF

    for i in range(n):

        array_xor ^= arr[i]
        total_xor ^= (i+1)

    return (array_xor ^ total_xor) & mask


print(optimal([1,2,3,4,5]))
    