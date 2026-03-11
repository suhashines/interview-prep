[Word Break](https://leetcode.com/problems/word-break/)

## Problem Statement
Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

## Example
**Example 1:**
```
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```
**Example 2:**
```
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
```
**Example 3:**
```
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
```

## Solution:

- We can use dynamic programming to solve this problem in `O(n^2)` time complexity.
- We will create a boolean array `dp` of size `n+1` where `n` is the length of the input string `s`. 

- `dp[i]` will be `true` if the substring `s[i:n]` can be segmented into words from the dictionary, and `false` otherwise.

- We will initialize `dp[n]` to `true` because an empty string can always be segmented.
- We will iterate through the string `s` from the end to the beginning and for each index `i`, we will check if there is a word `w` in the dictionary such that  `w` matches the substring starting from index `i` to the end of `[i + len(w)]`
- If we find such a word, we are sure that the substring `s[i:i + len(w)]` can be segmented, and if `dp[i + len(w)]` is also `true`, it means that the remaining substring can also be segmented. In this case, we will set `dp[i]` to `true` and break out of the loop.
- Finally, we will return the value of `dp[0]` which will indicate whether the entire string can be segmented or not.

```python
def wordBreak(s: str, wordDict: List[str]) -> bool:
    n = len(s)
    dp = [False] * (n + 1)
    dp[n] = True  # Base case: an empty string can always be segmented

    for i in range(n - 1, -1, -1):
        for word in wordDict:
            if i + len(word) <= n and s[i:i + len(word)] == word and dp[i + len(word)]:
                dp[i] = True
                break

    return dp[0]
```