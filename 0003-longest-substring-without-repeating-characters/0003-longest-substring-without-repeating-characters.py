class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        ret = 0
        for left in range(0, (len(s)-1)):
            local = 0
            seen = set()
            for right in range(left, len(s)):
                if s[right] in seen:
                    break
                else:
                    seen.add(s[right])
                    local+=1
                    ret = max(local, ret)
        return ret


                
                
