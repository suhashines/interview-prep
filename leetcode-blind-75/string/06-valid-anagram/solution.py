def isValidAnagram(s,t):

    charMap = {}

    for ch in s:
        charMap[ch] = 1 + charMap.get(ch,0)
    
    for ch in t:

        if ch not in charMap:
            return False
        
        if charMap[ch] > 0:
            charMap[ch] -= 1
        else:
            return False
    
    # now I have to check if all the chars has been used

    for key in charMap:
        if charMap[key]!=0:
            return False
    return True

s = "abcdef"
t = "acebdf"

print(isValidAnagram(s,t))