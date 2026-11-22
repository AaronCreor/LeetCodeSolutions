class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        maxv = 0
        left = 0
        vowel = 0

        for right in range(len(s)):
            if s[right] in vowels:
                vowel+=1
            if right - left + 1 == k:
                maxv = max(maxv, vowel)
                if s[left] in vowels:
                    vowel-=1
                left += 1
        return maxv

