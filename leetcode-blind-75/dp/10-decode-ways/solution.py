def decode_ways(s:str)->int:
    
    prev2 = 1
    prev1 = 1 if '1'<=s[0]<='9' else 0
    
    n = len(s)
    
    for i in range(1,n):
        
        curr = 0
        
        ch = s[i]
        
        two = s[i-1:i+1]
        
        print(f"considering {s[0:i+1] }")
        
        if "1"<=ch<="9" :
            curr += prev1
        
        if "10"<=two<="26":
           curr += prev2
        
        if(curr==0): return 0
        
        prev2 = prev1
        prev1 = curr
        
    return prev1


print(decode_ways("27"))