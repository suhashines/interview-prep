[Coin-Change-I](https://leetcode.com/problems/coin-change/)

## Problem Statement
You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.  You may assume that you have an infinite number of each kind of coin.

## Example
### Example 1:
```
Input: coins = [1,2,5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
```
### Example 2:
```
Input: coins = [2], amount = 3
Output: -1
Explanation: The amount of 3 cannot be made up just with coins of 2.
```

## Solution
- We can use dynamic programming to solve this problem. We will create an array `dp` where `dp[i]` represents the minimum number of coins needed to make up the amount `i`. We will initialize `dp[0]` to `0` since no coins are needed to make up the amount of `0`, and we will initialize all other values in `dp` to a large number (e.g., `amount + 1`) to represent that those amounts cannot be made up with the given coins.
- We will iterate through each coin in the `coins` array and for each coin, we will update the `dp` array for all amounts from the coin's value up to the `amount`. For each amount `i`, we will check if we can use the current coin to make up that amount by comparing `dp[i]` with `dp[i - coin] + 1`. If using the current coin results in a smaller number of coins, we will update `dp[i]`.

```python
def coinChange(coins, amount):
    # Initialize the dp array
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    
    # Update the dp array for each coin
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[amount] is still amount + 1, it means we cannot make up that amount
    return dp[amount] if dp[amount] != amount + 1 else -1
```

## Top-Down Approach
- We can also solve this problem using a top-down approach with memoization. We will define a recursive function that takes the remaining amount as an argument and returns the minimum number of coins needed to make up that amount. We will use a dictionary to store the results of previously computed amounts to avoid redundant calculations.

### Caveat
- The top-down approach can lead to a large number of recursive calls, especially for larger amounts, which may result in a stack overflow. The bottom-up approach is generally more efficient for this problem as it avoids the overhead of recursive calls and is easier to understand.

```python
def coinChange(coins, amount):
    memo = {}
    
    def helper(remaining):
        # Base case: if remaining is 0, no coins are needed
        if remaining == 0:
            return 0
        # If remaining is negative, return a large number to indicate it's not possible
        if remaining < 0:
            return float('inf')
        # Check if the result for the current remaining amount is already computed
        if remaining in memo:
            return memo[remaining]
        
        min_coins = float('inf')
        for coin in coins:
            min_coins = min(min_coins, helper(remaining - coin) + 1)
        
        memo[remaining] = min_coins
        return min_coins
    
    result = helper(amount)
    return result if result != float('inf') else -1
```