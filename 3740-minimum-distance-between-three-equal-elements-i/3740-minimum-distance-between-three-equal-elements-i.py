class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        minDist = -1
        runCount = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i]==nums[j] and i!=j):
                    for k in range(len(nums)):
                        if(nums[k]==nums[j] and k!=j and k!=i):
                            if (runCount == 0):
                                minDist = abs(i - j) + abs(j - k) + abs(k - i)
                            else:
                                minDist = min((minDist),(abs(i - j) + abs(j - k) + abs(k - i)))
                            runCount+=1
        return minDist
