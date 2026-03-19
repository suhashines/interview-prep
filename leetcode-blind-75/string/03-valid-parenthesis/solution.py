from collections import deque

def isValid(s):

    mp = {
        "(" : ")",
        "[" : "]",
        "{" :"}"
    }

    stack = deque()

    for i in range(len(s)):

        if s[i] in mp:
            # s[i] is an opening bracket
            # we put it in the stack
            stack.append(s[i])
        
        else:
            # s[i] is a closing bracket
            # we check if the top of the stack is the opening counterpart of s[i]
            top = stack[-1] if stack else None
            if mp.get(top) == s[i]:
                stack.pop()
            else:
                return False
    
    if stack:
        return False
    return True

s = "[[[[]]"
print(isValid(s))