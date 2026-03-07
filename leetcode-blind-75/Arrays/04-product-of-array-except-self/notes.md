[LeetCode Problem 238: Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

- The problem is asking us to return an array where each element at index `i` is the product of all the numbers in the input array except the one at index `i`. We are not allowed to use division and we need to achieve this in O(n) time complexity.


## Intuition
we can think of the product of all the numbers except the one at index `i` as the product of all the numbers to the left of `i` and the product of all the numbers to the right of `i`.

# Optimal Solution
- Calculate the product of all numbers to the left of each index and store it in an array.
- Calculate the product of all numbers to the right of each index and store it in another array.
- Multiply the corresponding elements from both arrays to get the final result.

```python
def productExceptSelf(nums):
    n = len(nums)
    left_products = [1] * n
    right_products = [1] * n        
    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]
    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]
    result = [1] * n
    for i in range(n):
        result[i] = left_products[i] * right_products[i]
    return result
```

- The above solution has a time complexity of `O(n)` and a space complexity of `O(n)` due to the two additional arrays used to store the left and right products.