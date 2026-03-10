[Binary sum of two integers](https://leetcode.com/problems/sum-of-two-integers/)

# Problem Statement
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.


## Intution:

- The sum of two numbers can be calculated using bitwise operators. The idea is to use the XOR operator to calculate the sum of the bits and the AND operator to calculate the carry.
- The XOR operator will give us the sum of the bits without considering the carry, while the AND operator will give us the carry. We can then shift the carry to the left and add it to the sum until there is no carry left.

## Caveat if implemented in Python:
- Python's integers are of arbitrary precision, which means they can grow beyond the typical 32-bit limit. This can lead to issues when performing bitwise operations, especially when dealing with negative numbers
- To handle this, we can use a mask to limit our calculations to 32 bits. This way, we can ensure that we are working within the bounds of a typical integer representation.

```python
def getSum(a: int, b: int) -> int:
    # Define a mask to limit our calculations to 32 bits
    mask = 0xFFFFFFFF
    while b != 0:
        # Calculate the sum of bits without considering the carry
        sum_without_carry = (a ^ b) & mask
        
        # Calculate the carry
        carry = ((a & b) << 1) & mask
        
        # Update a and b for the next iteration
        a, b = sum_without_carry, carry
    
    # If a is negative, we need to convert it back to a negative number
    return a if a <= 0x7FFFFFFF else ~(a ^ mask)
``` 