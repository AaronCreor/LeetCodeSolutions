class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            temp=""
            for j in range(i, len(s)):
                temp=temp+s[j]
                if temp[:] == temp[::-1]:
                    count=count+1
        return count
