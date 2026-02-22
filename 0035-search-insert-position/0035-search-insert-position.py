class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        pointer = 0
        while left <= right:
            pointer = (left+right) // 2
            if (nums[pointer] == target):
                return pointer
            if (nums[pointer] > target):
                right = pointer-1
            else:
                left = pointer+1
        return left