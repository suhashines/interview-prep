def longestPalindrome(s):

    n = len(s)
    res = ""
    resLen = 0

    # consider every character as the middle element of the palindrome
    # and expand outward

    for i in range(n):

        # odd-length palindrome
        l,r = i,i

        while l>=0 and r<n and s[l]==s[r]:

            # r-l+1 is the current length
            # we check if it's greater than resLen
            if (r-l+1) > resLen:
                #we update the resLen and res
                resLen = r - l + 1
                res = s[l:r+1]
            l -= 1
            r += 1 

        #even-length palindrome
        l,r = i,i+1
        
        while l>=0 and r<n and s[l]==s[r]:

            # r-l+1 is the current length
            # we check if it's greater than resLen
            if (r-l+1) > resLen:
                #we update the resLen and res
                resLen = r - l + 1
                res = s[l:r+1]
            l -= 1
            r += 1

    return res 

s = "cbbd"

print(longestPalindrome(s))