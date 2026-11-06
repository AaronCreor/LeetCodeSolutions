class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        ops = 0
        while True:
            check = 0
            for i in range(len(nums)):
                if nums[i] > 0:
                    check +=1
            if check == 0:
                return ops
            minVal = 99999999
            for i in range(len(nums)):
                if nums[i] > 0:
                    minVal = min(minVal, nums[i])
            for i in range(len(nums)):
                if ((nums[i]-minVal) >=0):
                    nums[i] = nums[i]-minVal
            ops+=1
            