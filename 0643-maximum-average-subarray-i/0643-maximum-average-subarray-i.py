class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #left = 0
        #right = left + k
        #maxVal = 0
        #firstRun = True
        #if(len(nums) == 1):
        #    return nums[0]
        #while right <= len(nums):
        #    temp = 0
        #    for x in range(left, right, 1):
        #        temp+=nums[x]
        #    if(firstRun):
        #       firstRun = False
        #       maxVal = temp/k
        #    maxVal = max(maxVal, temp/k)
        #    left = left+1
        #    right = right+1
        #return maxVal
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range (k, len(nums)):
            window_sum +=nums[i] - nums [i-k]
            max_sum = max(max_sum, window_sum)
        return max_sum / k