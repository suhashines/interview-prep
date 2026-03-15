[Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)

## Problem Statement
Given `n` nodes labeled from 0 to n - 1 and a list of edges, determine if the edges form a valid tree.

## Examples:
### Example 1:
```
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
```
### Example 2:
```
Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: true
```
### Example 3:
```
Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4],[4,0]]
Output: false
```
### Example 4:
```
Input: n = 5, edges = [[0,1],[2,3],[2,4],[3,4]]
Output: false
```

## Solution:

- A valid tree must have exactly `n - 1` edges, where `n` is the number of nodes. If the number of edges is not equal to `n - 1`, we can immediately return false.

- We can use a depth-first search (DFS) or breadth-first search (BFS) to check if the graph is fully connected. If we can visit all nodes starting from any node, then the graph is connected.

- Because we have already checked that the number of edges is `n - 1`, if the graph is connected, it cannot have any cycles. Therefore, we do not need to explicitly check for cycles.

- If the graph is connected and has `n - 1` edges, then it must be a valid tree. Therefore, we can return true.