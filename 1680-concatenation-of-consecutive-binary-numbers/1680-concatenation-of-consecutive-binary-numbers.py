class Solution:
    def concatenatedBinary(self, n: int) -> int:
        binStr = ""
        i = 1
        while (i <= n):
            binStr += format(i, 'b')
            i+=1
        ret = int(binStr, 2)
        return ret % ((10**9) +7)

        