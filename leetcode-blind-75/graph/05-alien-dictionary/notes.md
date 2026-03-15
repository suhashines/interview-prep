[Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)

## Problem Statement
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you. You are given a list of strings `words` from the alien language's dictionary, where the strings in `words` are sorted lexicographically by the rules of this new language.
Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

## Examples:
### Example 1:
```
Input: words = ["wrt","wrf","er","ett","rftt"], N=5 , K=5
Output: "wertf"
```
### Example 2:
```
Input: words = ["z","x"], N=2 , K=2
Output: "zx"
```

## Example 3: (No valid order)
```
Input: words = ["abc", "ab"], N=2 , K=3
Output: ""
```

## Solution:

- Create a graph and a degree map to represent the relationships between characters.
- Iterate through the list of words and compare adjacent words to determine the order of characters.
- Use a topological sort (Kahn's algorithm) to determine the order of characters based on the graph and degree map.

**An important thing to remember**

- We might not always get meaningful relationships between characters by comparing adjacent workds. For example, if we have `["abc","abcdef"]` , then we cannot determine the order of characters 'a', 'b', and 'c' since they appear in the same order in both words. In such cases, we should not add any edges to the graph for these characters.

- The dictionary might be invalid too, for example, if we have `["abc", "ab"]`, then there is no valid order of characters since "ab" should come before "abc". In such cases, we should return an empty string.