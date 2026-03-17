[Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

## Problem Statement
You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.

## Examples:
### Example 1:
```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked-list:
1->1->2->3->4->4->5->6
```
### Example 2:
```
Input: lists = []
Output: []
```

## Solution

- **Brute Force**: We can merge the linked-lists one by one. We can start with the first two linked-lists and merge them into one sorted linked-list. Then we can merge the result with the next linked-list and so on until we have merged all the linked-lists. The time complexity of this approach is `O(N*K)` where `N` is the total number of nodes in all the linked-lists and `K` is the number of linked-lists.

- **Using Divide and Conquer**: We can use the divide and conquer approach to merge the linked-lists. We can divide the linked-lists into two halves and merge them recursively. The time complexity of this approach is `O(N*logK)` where `N` is the total number of nodes in all the linked-lists and `K` is the number of linked-lists.