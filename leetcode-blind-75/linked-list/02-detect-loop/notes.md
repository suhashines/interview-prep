[Detect Loop in Linked List](https://leetcode.com/problems/linked-list-cycle/)

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it.

## Examples
### Example 1
```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the second node
```

### Example 2
```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the first node.
```
### Example 3
```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

## Solution

- To solve this problem, we can use the Floyd’s Tortoise and Hare algorithm, which is a common technique for detecting cycles in linked lists. The idea is to use two pointers, one slow (tortoise) and one fast (hare). The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. If there is a cycle in the linked list, the fast pointer will eventually meet the slow pointer. If there is no cycle, the fast pointer will reach the end of the list.

Look at the picture below:

![Floyd's Tortoise and Hare Algorithm](https://static.takeuforward.org/content/yy11.png-xi4uyw4p)

- Now if there is no cycle, there can be two cases:
  1. The fast pointer reaches the end of the list (i.e., `fast` becomes `null`). It happens when the linked list has an even number of nodes.
  2. The fast pointer reaches the last node (i.e., `fast.next` becomes `null`). It happens when the linked list has an odd number of nodes. Watch the image below for better understanding.

![Floyd's Tortoise and Hare Algorithm](https://static.takeuforward.org/content/-aCOZk2MH)