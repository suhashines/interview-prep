def min_number_of_coins(amount:int,coins:list[int]):

    n = len(coins) 

    dp = [[-1] * (amount + 1) for _ in range(n + 1)]

    ans = helper(amount,coins,dp,n)

    print(f"after helper dp: {dp}")

    if(ans!=float('inf')):
        return ans
    return -1

def helper(amt:int,coins:list[int],dp:list[list[int]],n:int):

    if(amt==0):
        dp[n][0] = 0
        return 0
    
    if(n==0):

        dp[0][amt] = float('inf')
        return float('inf')
    
    if(dp[n][amt]!=-1):
        # we've already solved the subproblem
        return dp[n][amt]
    
    # we need to solve the subproblem

    # can we take the nth coin?

    if(amt-coins[n-1]<0):
        # not possible to take the nth coin
        dp[n][amt] = helper(amt,coins,dp,n-1)
        return dp[n][amt]
    
    # we can take the nth coin

    dp[n][amt] = min(
        helper(amt,coins,dp,n-1), # min no of ways without taking the nth coin
        helper(amt-coins[n-1],coins,dp,n) + 1 # min no of ways taking the nth coin
    )

    return dp[n][amt]

print(min_number_of_coins(11,[1,2,5]))
print(min_number_of_coins(3,[2]))
print(min_number_of_coins(10,[9,2]))