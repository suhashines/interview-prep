def isPalindrome(s:str):

    n = len(s)
    l,r = 0,n-1
    
    while l<r:

        while l<r and not s[l].isalnum():
            l += 1
        
        while l<r and not s[r].isalnum():
            r -= 1
        
        # after this loop both of them are either alphanumeric or both points to the same
        # non-alphanumeric character

        if s[l].lower() != s[r].lower():
            return False
        
        l += 1
        r -= 1
    return True

s = "A  man  , a   plan,,,,,;::::*##(#)#*#(#(#)) a canal: Panama"
# s = "race a car"
# s = " "
s= "#%$%$^%^&%&^%*&^*"
print(isPalindrome(s))
