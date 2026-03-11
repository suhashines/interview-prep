def combination_sum(arr:list[int],target:int)->list[list[int]]:

    res = []

    n = len(arr)

    def dfs(i:int,target:int,cur:list):

        if(target<0 or i>=n): return

        if(target==0):
            res.append(cur.copy())
            return

        # make a decision about the ith number
        cur.append(arr[i])
        dfs(i,target-arr[i],cur)
        cur.pop()
        dfs(i+1,target,cur)

    dfs(0,target,[])
    return res

print(combination_sum([2,3,6,7],target=7))
                        
        
