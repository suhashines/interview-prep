[Find Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)

## Problem Statement
Given an array of intervals `intervals` where `intervals[i] = [starti, endi]`, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

## Examples:

### Example 1:
```
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
```
### Example 2:
```
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
```

## Solution

- Sort the intervals based on their end time.
- Initialize a variable `count` to keep track of the number of non-overlapping intervals and a variable `end` to keep track of the end time of the last added interval.
- Iterate through the sorted intervals:
    - If the start time of the current interval is greater than or equal to `end`, it means there is no overlap, so we can include this interval and update `end` to the end time of the current interval.
    - Otherwise, it means there is an overlap, so we need to remove this interval and increment the count of removed intervals.