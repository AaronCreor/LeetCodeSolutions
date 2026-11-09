class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ret = 0
        left = 0
        seen = set()
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            ret = max(ret, right-left + 1)
        return ret

                
                
