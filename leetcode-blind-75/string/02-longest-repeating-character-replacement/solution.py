def characterReplacement(s:str,k:int):
    l = 0
    maxf = 0
    count = {}
    res = 0

    for r in range(len(s)):

        count[s[r]] = 1 + count.get(s[r],0)
        # if the key doesn't exist return 0

        # we keep track of the maximum frequency we've seen so far
        maxf = max(maxf,count[s[r]])

        # now we check the validity of the window
        # window is valid if length(window) - freq of the common char <= k

        while (r - l + 1) - maxf > k:
            # decrease the freq of s[l] since they're getting removed from the window
            count[s[l]] -= 1
            # since we're changing freq map, we need to readjust the maxf of the current window
            # but the highest window we can get is k + maxf
            # so the res wil only change if maxf increase
            l += 1
        res = max(res,r-l+1)

    return res

s = "AABABBA"
k = 2

print(characterReplacement(s,k))