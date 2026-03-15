[Course Schedule](https://leetcode.com/problems/course-schedule/)

# Problem Statement
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses-1`. You are given an array `prerequisites` where `prerequisites[i] = [a_i, b_i]` indicates that you must take course `b_i` before taking course `a_i`.
Return `true` if you can finish all courses. Otherwise, return `false`.

## Examples:
### Example 1:
```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true        
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.
```
### Example 2:
```
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
```

## Prerequisite

## Topological Sort
 A linear ordering of vertices in a directed graph such that for every directed edge from vertex A to vertex B, vertex A comes before vertex B in the ordering.

## Examples:

- Consider the directed graph below
```
    0
   / \
  1   2
 / \ / \
3   4   5
```

- A valid topological ordering for this graph could be: `0, 1, 2, 3, 4, 5` or `0, 2, 5, 1, 4,3`.

## How to find topological order? 

- **Using DFS**: Perform a depth-first search on the graph, and as you finish visiting each vertex, add it to a stack. Once all vertices are visited, the stack will contain the vertices in reverse topological order.

- **Using Kahn's Algorithm**: This algorithm uses a queue to keep track of vertices with no incoming edges. Start by adding all vertices with no incoming edges to the queue. Then, repeatedly remove a vertex from the queue, add it to the topological order, and decrease the in-degree of its neighboring vertices. If any neighboring vertex's in-degree becomes zero, add it to the queue.

## let's look at a simulation of the Kahn's Algorithm on the graph above:
1. Start with vertices that have no incoming edges: `0`.
2. Remove `0` from the queue and add it to the topological order: `0`.
3. Decrease the in-degree of its neighbors `1` and `2`. Now, `1` and `2` have no incoming edges, so add them to the queue: `1, 2`.
4. Remove `1` from the queue and add it to the topological order: `0, 1`.
5. Decrease the in-degree of its neighbors `3` and `4`. Now,`3` and `4` have no incoming edges, so add them to the queue: `2, 3, 4`.
6. Remove `2` from the queue and add it to the topological order: `0, 1, 2`.
7. Decrease the in-degree of its neighbor `5`. Now, `5` has no incoming edges, so add it to the queue: `3, 4, 5`.
8. Remove `3` from the queue and add it to the topological order: `0, 1, 2, 3`.
9. Remove `4` from the queue and add it to the topological order: `0, 1, 2, 3, 4`.
10. Remove `5` from the queue and add it to the topological order: `0, 1, 2, 3, 4, 5`.
