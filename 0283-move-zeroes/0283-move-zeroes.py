class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #for i in range(len(nums)-1, -1, -1):
        #    if(nums[i] == 0):
        #       nums.append(nums.pop(i))
        #return nums
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
        return nums
        