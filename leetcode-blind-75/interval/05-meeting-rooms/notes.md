[Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)

## Problem Statement
Given an array of meeting time intervals `intervals` where `intervals[i] = [starti, endi]`, determine if a person could attend all meetings.

## Examples:
### Example 1:
```
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Explanation: A person cannot attend all meetings because the first meeting overlaps with the second and third meetings.
```
### Example 2:
```
Input: intervals = [[7,10],[2,4]]
Output: true
Explanation: A person can attend all meetings because there are no overlapping meetings.
```

## Solution

- Sort the intervals based on their start time.
- Iterate through the sorted intervals and check if there is any overlap between consecutive intervals:
    - If the end time of the current interval is greater than the start time of the next interval, it means there is an overlap, and we can return false.   
- If we finish iterating through all intervals without finding any overlaps, we can return true.