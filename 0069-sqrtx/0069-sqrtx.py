class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        if x == 2:
            return 1
        i=1
        z = 1
        while z == 1:
            if (i*i == x):
                return i
            if (i*i > x):
                return i - 1

            else:
                i=i+1
