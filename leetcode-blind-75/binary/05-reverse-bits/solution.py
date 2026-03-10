def optimal(num:int)->int:
    
    res = 0
    mask = 0xFFFFFFFF

    for i in range(32):

        lsb = (num >> i) & 1
        res = (res << 1) | lsb

    return res & mask 

print(optimal(43261596))