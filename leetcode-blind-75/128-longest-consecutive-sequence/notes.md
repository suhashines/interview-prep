[LeetCode Problem 128: Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)


**Unordered set has search complexity of O(1) on average, so we can check if a number exists in the set in constant time.**

## Optimal Solution

- We can iterate through the array and for each number, we can check if it is the start of a sequence by checking if the previous number `(num - 1)` exists in the set. If it does not exist, then we can start counting the length of the sequence by checking for the next numbers `(num + 1, num + 2, etc.)` until we find a number that does not exist in the set.