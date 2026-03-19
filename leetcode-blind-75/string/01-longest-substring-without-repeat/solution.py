def withoutRepeat(s:str):

    # we keep a hashmap to keep track of the last seen index of a character
    mp = {}

    start= 0

    maxCount = 0

    for end in range(len(s)):

        # print(f"observing substring {s[start:end+1]}")
        # print(f"current map {mp}")

        if s[end] in mp:
            # find the previous index where s[end] occured
            idx = mp[s[end]]
            # move start to the next index only if the next idx > start
            # it ensures we never move start backward
            start = max(start,idx+1)
            # update the value in mp
        
        # update the index of the character
        mp[s[end]] = end

        # print(f"updated start pointer {start}")

        # print(f"current length {end-start+1} and max length {maxCount}")
        maxCount = max(maxCount,end-start+1)
        end += 1
        # print("-"*10)
    return maxCount

s = "abcabcbb"
s = "bbbbb"
s = "pwwkew"
s = "abba"

print(withoutRepeat(s))