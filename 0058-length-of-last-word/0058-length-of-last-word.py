class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastCount = 0
        check = 0
        for i in range(len(s)):
            if(s[i] == ' '):
                check = 1
            else:
                if(check == 1):
                    lastCount = 0
                lastCount = lastCount+1
                check = 0
        return lastCount