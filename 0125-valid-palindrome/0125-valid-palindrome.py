class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        clean = "".join(ch for ch in s if ch.isalnum())
        if(clean == clean[::-1]):
            return True
        else:
            return False
        
        