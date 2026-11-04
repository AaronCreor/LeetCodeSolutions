class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        numsS = sorted(nums)
        left = 0
        right = 0
        if (numsS == nums):
            return 0
        for i in range(len(nums)):
            if(nums[i] == numsS[i]):
                continue
            else:
                left = i
                break
        for i in range(len(nums)-1, 0, -1):
            if (nums[i] == numsS[i]):
                continue
            else:
                right = i
                break
        return (right-left)+1