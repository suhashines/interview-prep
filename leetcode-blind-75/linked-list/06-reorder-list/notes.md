[Reorder List](https://leetcode.com/problems/reorder-list/)

## Problem Statement
You are given the head of a singly linked list. Reorder the list such that it follows the pattern: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

## Examples:
### Example 1:
```
Input: head = [1,2,3,4]
Output: [1,4,2,3]
```
### Example 2:
```
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```

## Solution

- **Two Pointers**: We can use two pointers to find the middle of the linked list and then reverse the second half. After that, we can merge the two halves by alternating nodes from each half. The time complexity of this approach is `O(N)` where `N` is the total number of nodes in the linked list.

1. Find the middle of the linked list using the slow and fast pointer technique.

2. When `fast` reaches the end of the linked list, `slow` will be at the middle. We can then reverse the second half of the linked list starting from `slow.next`.

3. Don't forget to set `slow.next` to `null` to split the linked list into two halves.

4. Finally, we can merge the two halves by alternating nodes from each half until we have merged all the nodes.