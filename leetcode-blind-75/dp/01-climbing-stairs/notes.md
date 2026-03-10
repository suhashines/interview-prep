[Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

## Problem Statement
You are climbing a staircase. It takes `n` steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

## Optimal Solution

- Think of the problem as a tree where each node represents a step and the edges represent the possible moves (1 or 2 steps).
- The number of ways to reach the top from step `n` can be expressed as the sum of the ways to reach the top from step `n-1` and step `n-2`.
- This leads to the recurrence relation: `ways(n) = ways(n-1) + ways(n-2)`.
- Base cases: `ways(0) = 1` (there's one way to stay at the bottom) and `ways(1) = 1` (there's one way to climb one step).

- since the subproblems overlap, we can use dynamic programming to store the results of previously computed subproblems to avoid redundant calculations.