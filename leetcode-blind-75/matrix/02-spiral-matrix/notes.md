[Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)

## Problem Statement
Given an `m x n` matrix, return all elements of the matrix in spiral order.

## Example 1:
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```
## Example 2:
```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

## Solution

- We can use four pointers to keep track of the boundaries of the matrix: `top`, `bottom`, `left`, and `right`. Initially, `top` is set to 0, `bottom` is set to `m`, `left` is set to 0, and `right` is set to `n`.

- We can then iterate through the matrix in a spiral order by following these steps:
  1. Traverse from `left` to `right` along the `top` row, and then increment `top` by 1.
  2. Traverse from `top` to `bottom` along the `right-1` column, and then decrement `right` by 1.
  3. If `top` is still less than `bottom`, traverse from `right-1` to `left` along the `bottom` row, and then decrement `bottom` by 1.
  4. If `left` is still less than `right`, traverse from `bottom-1` to `top` along the `left` column, and then increment `left` by 1.