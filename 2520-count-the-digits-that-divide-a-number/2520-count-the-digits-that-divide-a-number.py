class Solution:
    def countDigits(self, num: int) -> int:
        z = 0
        for i in str(num):
            if (num % int(i) == 0):
                z=z+1
        return z
