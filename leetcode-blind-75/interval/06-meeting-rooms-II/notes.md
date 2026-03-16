[Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)

## Problem Statement
Given an array of meeting time intervals `intervals` where `intervals[i] = [starti, endi]`, determine the minimum number of conference rooms required to host all meetings.

## Examples:
### Example 1:
```
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Explanation: We need two conference rooms. One for [0,30] and another for [5,10] and [15,20].
```
### Example 2:
```
Input: intervals = [[7,10],[2,4]]
Output: 1
Explanation: We only need one conference room.
```

## Solution

- The idea is to keep track of the number of ongoing meetings at any given time. We can achieve this by separating the start and end times of the meetings and sorting them.

- Create two separate arrays: `startTimes` and `endTimes`, and populate them with the start and end times of the meetings, respectively.
- Sort both `startTimes` and `endTimes` arrays.
- Initialize two pointers, `startPointer` and `endPointer`, to keep track of the current position in the `startTimes` and `endTimes` arrays, respectively. Also, initialize a variable `rooms` to keep track of the number of rooms needed and a variable `maxRooms` to keep track of the maximum number of rooms needed at any time.

- Iterate through the `startTimes` array:
    - If the current start time is less than the current end time, it means a new meeting has started before the previous one has ended, so we need an additional room. Increment `rooms` and move the `startPointer` to the next start time.
    - Otherwise, it means a meeting has ended before the next one starts, so we can free up a room. Decrement `rooms` and move the `endPointer` to the next end time.
    - Update `maxRooms` to be the maximum of `maxRooms` and `rooms`.
- After iterating through all the start times, `maxRooms` will contain the minimum number of conference rooms required to host all meetings. Return `maxRooms`.

