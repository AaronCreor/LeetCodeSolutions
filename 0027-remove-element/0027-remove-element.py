class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            for i in range(len(nums)):
                if nums[i] == val:
                    nums.pop(i)
                    break
        return len(nums)