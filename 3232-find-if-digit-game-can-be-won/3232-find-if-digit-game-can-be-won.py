class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = 0
        double = 0
        for i in nums:
            if i >= 10:
                double = double+i
            else:
                single = single+i
        if single != double:
            return True
        else:
            return False