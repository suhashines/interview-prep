def tabulation(s:str,wordDict:list[str])->bool:
    
    n = len(s)

    dp = [False]*(n+1)
    dp[n] = True

    for i in range(n-1,-1,-1):

        for w in wordDict:

            l = len(w)

            if(i+l<=n and s[i:i+l]==w):

                dp[i] = dp[i+l]
            
            if dp[i] :
                # dp[i] true means that starting from the ith index of s
                # a valid break exists
                # hence we don't need to look further
                break

    return dp[0]

word = "cars"
wordDict = ["car","ca","rs"]

print(tabulation(word,wordDict))