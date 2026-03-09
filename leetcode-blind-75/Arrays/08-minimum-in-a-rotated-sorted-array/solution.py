def optimal(a:list,l:int,h:int):

    if(l==h): return a[l]

    m = (l+h)//2

    # now we have to figure out which part of the array is sorted

    if(a[l]<=a[m]):
        #left side is sorted

        return min(a[l],optimal(a,m+1,h))
    else:

        # right side is sorted
        return min(a[m],optimal(a,l,m-1))


def find_min(a:list):

    return optimal(a,0,len(a)-1)

print(find_min([5,6,-1,0,2,3,3,4]))