class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ret = 0
        for left in range(0, len(s)):
            local = 0
            seen = set()
            for right in range(left, len(s)):
                if s[right] not in seen:
                    seen.add(s[right])
                    local=local+1
                    ret = max(local, ret)
                else:
                    break
        return ret
                
                
