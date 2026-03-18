[Word Search](https://leetcode.com/problems/word-search/)

## Problem Statement
Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.  
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

## Example 1:
```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```
## Example 2:
```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
```
## Example 3:
```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
```
## Solution

- There is no efficient algorithm to solve this problem, so we can use backtracking to explore all possible paths in the grid.

- We can define a recursive function that takes the current position in the grid and the index of the current character in the word. The function will check if the current character matches the character in the grid at the current position. If it does, we can recursively call the function for all adjacent cells (up, down, left, right) and check if any of those calls return true.