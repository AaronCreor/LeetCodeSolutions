class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1]  * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
    



        
        
        
        #res = []
        #for i in range(len(nums)):
        #    res.append(prod((nums[:i] + nums[i+1:])))
        #return(res)
