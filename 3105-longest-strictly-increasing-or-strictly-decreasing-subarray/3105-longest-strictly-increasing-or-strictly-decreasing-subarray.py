class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increase = [nums[0]]
        decrease = [nums[0]]
        localIncrease =[nums[0]]
        localDecrease = [nums[0]]
        for i in range(1, len(nums)):
            if (nums[i] > nums[i-1]):
                localIncrease.append(nums[i])
                if(len(increase) > len(localIncrease)):
                    increase = increase
                else:
                    increase = localIncrease
                localDecrease = [nums[i]]
            if (nums[i] < nums[i-1]):
                localDecrease.append(nums[i])
                if(len(decrease) > len(localDecrease)):
                    decrease = decrease
                else:
                    decrease = localDecrease
                localIncrease = [nums[i]]
            if nums[i] == nums[i-1]:
                localIncrease = [nums[i]]
                localDecrease = [nums[i]]
        if len(increase) > len(decrease):
            return len(increase)
        else:
            return len(decrease)
            
