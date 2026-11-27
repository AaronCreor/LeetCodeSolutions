class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        if s == "":
            return 0
        count = 0
        temp = s[0]
        for i in range(1, len(s), 1):
            if s[i] != temp:
                count+=1
                temp = s[i]
            else:
                temp = s[i]
                continue
        return count
