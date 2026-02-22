class Solution:
    def binaryGap(self, n: int) -> int:
        counter = 0
        counterMax = 0
        while n & 1 != 1:#iterate to first 1
            n = n >> 1
            print(n)
        if(n==0):
            return 0
        while n > 0:
            if(n & 1 != 1):
                n = n >> 1
                counter=counter+1
                print(counter)
            else:
                n = n >> 1
                counterMax=max(counter,counterMax)
                counter=1
        return counterMax
            #1011
            #0010