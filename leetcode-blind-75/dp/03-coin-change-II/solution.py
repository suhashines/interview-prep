def tabulation(amt:int,coins:list[int])->int:

    dp = [0]*(amt+1)

    dp[0] = 1

    for coin in coins:

        for i in range(coin,amt+1):

            dp[i] = dp[i]+dp[i-coin]
    
    return dp[amt]

print(tabulation(5,[1,2,5]))