class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        numSet = set(nums)
        i = 0
        while True:
            if i in numSet:
                i+=1
                continue
            else:
                return i