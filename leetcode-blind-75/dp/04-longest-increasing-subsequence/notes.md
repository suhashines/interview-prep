[Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)

## Problem Statement
Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

## Example
**Example 1:**
```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
```
**Example 2:**
```
Input: nums = [0,1,0,3,2,3]
Output: 4
Explanation: The longest increasing subsequence is [0,1,2,3], therefore the length is 4.
```

## Solution:

- We can use binary-search to solve this problem in `O(n log n)` time complexity.
- We will maintain a list `sub` which will store the longest increasing subsequence found so far.
- We will iterate through each number in the input array `nums` and for each number,
    - If the number is greater than the last element in `sub`, we will append it to `sub`.
    - Otherwise, we will find the index of the smallest element in `sub` which is greater than or equal to the current number using binary search and replace that element with the current number.
- Finally, the length of `sub` will give us the length of the longest increasing subsequence.