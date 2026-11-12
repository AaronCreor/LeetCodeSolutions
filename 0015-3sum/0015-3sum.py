class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i -1]:
                continue #short circuit duplicates
            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = val + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res

        #ret = set()
        #for i in range(len(nums)-2):
        #    for j in range(i+1, len(nums)-1):
        #        for k in range(j+1, len(nums)):
        #            if ((nums[i] + nums[j] + nums[k]) == 0):
        #                if(i!=j and i!=k and j!=k):
        #                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
        #                    ret.add(triplet)
        #return [list(t) for t in ret]
