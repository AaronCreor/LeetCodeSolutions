class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        elementSum = 0
        digitSum = 0
        for i in nums:
            elementSum += i
        for i in nums:
            i = str(i)
            for j in i:
                digitSum += int(j)
                
        return abs(elementSum - digitSum)