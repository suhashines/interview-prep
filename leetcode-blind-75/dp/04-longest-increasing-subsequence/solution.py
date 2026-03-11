def search(a:list[int],l:int,h:int,k:int):
    # returns the index of smallest num in 'a' such that num>=k 
    if(l==h):
        if(k<=a[l]): return l
        return -1
    
    m = (l+h)//2

    if(a[m]==k): return m

    if(a[m]<k): return search(a,m+1,h,k)

    return search(a,l,m,k)


def lis(a:list[int])->int:

    tmp = []
    cnt = 0
    n = len(a)

    for i in range(n):

        if(i==0):
            tmp.append(a[i])
            cnt += 1
            continue

        if(a[i]==tmp[-1]): continue

        if(a[i]>tmp[-1]):
            # taking a[i] will increase the lis
            tmp.append(a[i])
            cnt += 1
        else:
            # we need to find the smallest number num in tmp such that num>=a[i]
            # and replace it with a[i]
            tmp[search(tmp,0,cnt-1,a[i])] = a[i]
        print(f"after iter {i} , tmp is {tmp}")
    return cnt


a =  [10, 9, 2, 5, 3, 7, 101, 18]   
print(lis(a))