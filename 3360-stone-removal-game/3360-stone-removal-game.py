class Solution:
    def canAliceWin(self, n: int) -> bool:
        start = 10
        alice = False
        while start > 0 and n >= start and n > 0:
            n = n - start
            start = start-1
            print(n)
            print(start)
            
            if alice is True:
                alice = False
            else:
                alice = True
            if n == 0:
                return alice
        return alice
            

