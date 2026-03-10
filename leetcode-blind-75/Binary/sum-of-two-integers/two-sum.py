def getSum(a: int, b: int) -> int:
    
    mask = 0xffffffff  # 32-bit mask
    
    while b != 0:
        sum_ = (a ^ b) & mask
        carry = ((a & b) << 1) & mask
        
        a = sum_
        b = carry
    
    # handle negative numbers
    if a > 0x7fffffff: # looking at the sign bit, if sign bit is 1, then it's negative
        return ~(a ^ mask)
    # a ^ mask shifts the bit and using ~ we restore python's negative representation
    
    return a