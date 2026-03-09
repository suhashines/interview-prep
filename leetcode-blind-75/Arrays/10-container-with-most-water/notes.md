[Container with most water](https://leetcode.com/problems/container-with-most-water/)

## Problem statement
Given n non-negative integers `height[0], height[1], ..., height[n-1]` where each represents a point at coordinate (i, height[i]). n vertical lines are drawn such that the two endpoints of line i is at (i, 0) and (i, height[i]). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

## Solution

- Initialize two pointers, `left` and `right`, at the beginning and end of the array, respectively.
- Initialize a variable `max_area` to keep track of the maximum area found.
- While `left` is less than `right`:
    - Calculate the area formed by the lines at `left` and `right` using the formula: `area = min(height[left], height[right]) * (right - left)`.
    - Update `max_area` if the calculated area is greater than the current `max_area`.
    - Move the pointer that points to the shorter line inward (i.e., if `height[left] < height[right]`, move `left` to the right; otherwise, move `right` to the left).

[Find the solution article here](https://leetcode.com/problems/container-with-most-water/solutions/7246589/solution-by-la_castille-1not/)