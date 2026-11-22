class Solution:
    def checkString(self, s: str) -> bool:
        seen = ""
        for i in s:
            if seen == "b" and i == "a":
                return False
            seen = i
        return True