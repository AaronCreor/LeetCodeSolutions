class Solution:
    def maxArea(self, height: list[int]) -> int:
        #o(n^2) failed on time
        ret = 0
        left = 0
        right = len(height)-1
        while left < right:
            ret = max(((right - left)*min(height[left], height[right])), ret)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return ret
        