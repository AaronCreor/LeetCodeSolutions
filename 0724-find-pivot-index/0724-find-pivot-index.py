class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        tot = sum(nums)
        running = 0
        for i in range(len(nums)):
            if running == (tot-nums[i])/2:
                return i
            running+=nums[i]
        return -1