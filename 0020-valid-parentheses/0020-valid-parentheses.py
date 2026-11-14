from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = {")":"(","}":"{","]":"["}
        for c in s:
            if stack and c in openToClose:
                if stack[-1] == openToClose[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if stack:
             return False 
        else:
             return True
            
