def brute(a:list):

    max_area = float('-inf')

    n = len(a)

    for i in range(n):

        for j in range(i+1,n):

            area = min(a[i],a[j])*(j-i)

            max_area = max(max_area,area)

    return max_area


def optimal(a:list):

    max_area = float('-inf')
    n = len(a)
    
    l,r = 0,n-1

    while(l<r):

        res = min(a[l],a[r])*(r-l)
        max_area = max(max_area,res)

        if(a[l]<=a[r]):
            # it means the left height is becoming the bottleneck
            # so any future pairing with the left height will result in reduced width and no height gain
            l+=1
        else:
            r-=1

    return max_area


a=[1,2,4,3]
print(brute(a))
print(optimal(a))