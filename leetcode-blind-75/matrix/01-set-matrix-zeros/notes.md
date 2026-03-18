[Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)

## Problem Statement
Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s.
You must do it in place.

## Example 1:
```
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```
## Example 2:
```
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

## Solution

- The idea is to use the first row and first column of the matrix as markers to indicate whether a particular row or column should be set to zero.

- We can iterate through the matrix and whenever we encounter a zero, we can mark the corresponding row and column in the first row and first column.

- Notice that we need to keep track of whether the first row and first column themselves should be set to zero, as they are being used as markers. if we only use `[0][0]` to mark the first row and first column, we won't be able to distinguish between the two. Therefore, we can use `[0][0]` as a marker for the first row and for the first column we can use a separate boolean variable.

