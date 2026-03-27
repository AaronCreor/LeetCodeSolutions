class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            nStr = str(num)
            x = 0
            for i in range(len(nStr)):
                x+=int(nStr[i])
            num = x
        return num