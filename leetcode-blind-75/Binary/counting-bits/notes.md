[Counting Bits](https://leetcode.com/problems/counting-bits/)

## Problem Statement
Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` (0 <= i <= n), `ans[i]` is the number of 1's in the binary representation of `i`.

## Optimal Solution


- Time Complexity: O(n)

- Look at the pattern below:

| i (Decimal) | i (Binary) | Number of 1's |
|-------------|------------|----------------|
| 0           | 0          | 0              |
| 1           | 1          | 1              |
| 2           | 10         | 1              |
| 3           | 11         | 2              |
| 4           | 100        | 1              |   
| 5           | 101        | 2              |
| 6           | 110        | 2              |
| 7           | 111        | 3              |
| 8           | 1000       | 1              |

- when we are calculating ans[4] = 1 + ans[4-4]
- similarly, ans[5] = 1 + ans[5-4]
- ans[6] = 1 + ans[6-4]

- Then when we reached 8, we can see that ans[8] = 1 + ans[8-8]
- similarly, ans[9] = 1 + ans[9-8]
- ans[10] = 1 + ans[10-8]

- We can see that when we are calculating ans[i], we are adding 1 to ans[i - offset], where offset is the largest power of 2 less than or equal to i.

- so what we can do is to keep track of the largest power of 2 less than or equal to i, and use that to calculate ans[i].

```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        offset = 1
        
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset *= 2
            ans[i] = 1 + ans[i - offset]
        
        return ans
```
