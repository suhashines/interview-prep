[Maximum Subarray Product](https://leetcode.com/problems/maximum-product-subarray/description/)

## Optimal Solution

### Using prefix and suffix products

- We can calculate the prefix product and suffix product for each element in the array. The prefix product is the product of all elements to the left of the current element, and the suffix product is the product of all elements to the right of the current element.

- while calculating the prefix and suffix products ,we can keep track of the maximum product encountered so far. We call them `max_prefix` and `max_suffix` respectively.

- finally the maximum product of a subarray will be the maximum of `max_prefix` and `max_suffix`.