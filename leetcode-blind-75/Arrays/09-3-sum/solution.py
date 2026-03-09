def brute_force(a:list):

    n = len(a)
    ans = set()

    for i in range(n):

        for j in range(i+1,n):

            for k in range(j+1,n):

                if(a[i]+a[j]+a[k]==0):
                   t = tuple(sorted([a[i],a[j],a[k]]))
                   ans.add(t) 
    
    return list(list(tup) for tup in ans)


def better(a:list):
    n = len(a)
    ans = set()

    for i in range(n):

        st = set()

        for j in range(i+1,n):

            t = -(a[i]+a[j])
            if(t in st):
                tup = tuple(sorted([a[i],a[j],t]))
                ans.add(tup)
            
            st.add(a[j])

    return list(list(tup) for tup in ans)

def optimal(a:list):

    a = sorted(a)

    n = len(a)

    ans = []
   
    for i in range(n):

        # skip the duplicate first element so that ans remains unique

        if(i>0 and a[i-1]==a[i]): continue

        l,r = i+1,n-1

        while(l<r):

            total = a[i]+a[l]+a[r]

            if(total==0):
                ans.append([a[i],a[l],a[r]])
                l+=1
                r-=1

                # # skip duplicates for left

                while(l<r and a[l-1]==a[l]): 
                    l+=1
                
                # skip duplicates for right
                while(r>l and a[r-1]==a[r]):
                    r-=1

                # consider the example of [-1,0,0,1,0,0,1], without the above check, we cannot ensure that our 2nd and 3rd element are unique

            elif(total<0):
                l+=1
            else:
                r-=1

    return ans


a = [-1,0,0,1,0,0,1]
print(brute_force(a))
print(better(a))
print(optimal(a))