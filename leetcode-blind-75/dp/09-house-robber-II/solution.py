from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # LeetCode House Robber II (circular houses)
        # We cannot rob both the first and last house.
        # Equivalent to max of robbing [0..n-2] or [1..n-1].

        def rob_linear(arr: List[int], start: int, end: int) -> int:
            # Rob houses in a linear street [start, end) (end exclusive).
            prev2 = 0
            prev1 = 0
            for i in range(start, end):
                curr = max(prev1, prev2 + arr[i])
                prev2, prev1 = prev1, curr
            return prev1

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        return max(rob_linear(nums, 0, n - 1), rob_linear(nums, 1, n))
    
arr = [2,1,4,9]

soln = Solution()

print(soln.rob(arr))