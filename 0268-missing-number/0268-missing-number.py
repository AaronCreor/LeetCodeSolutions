class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        total = int(((len(nums) * (len(nums) + 1))/2))
        for i in nums:
            total = total - i
        return total