def memoization(str1:str,str2:str)->int:

    n = len(str1)
    m = len(str2)

    dp = [[-1]*(m+1) for _ in range(n+1)]

    def LCS(n:int,m:int):

        if(n==0 or m==0):
            dp[n][m] = 0
            return 0
        
        if(dp[n][m]!=-1):
            # we've already solved the subproblem
            return dp[n][m]
        
        if(str1[n-1]==str2[m-1]):
            dp[n][m] = LCS(n-1,m-1) + 1
            return dp[n][m]
        
        dp[n][m] = max(
            LCS(n-1,m) , LCS(n,m-1)
        )

        return dp[n][m]
    
    def print_LCS(dp:list[list[int]],n:int,m:int)->str:

        if(n==0 or m==0):
            return 

        if(str1[n-1]==str2[m-1]):
            # we had a match at position n,m
            print_LCS(dp,n-1,m-1)
            print(f"{str1[n-1]}",end="")
        
        elif(dp[n][m]==dp[n-1][m]):

            # we came from the top
            print_LCS(dp,n-1,m)
        else:
            # we came from the left
            print_LCS(dp,n,m-1)

    lcs = LCS(n,m)    
    print_LCS(dp,n,m)
    print()
    return lcs


str1 = "daenyris stormborn"
str2 = "protector of the realm" 

print(memoization(str1,str2))