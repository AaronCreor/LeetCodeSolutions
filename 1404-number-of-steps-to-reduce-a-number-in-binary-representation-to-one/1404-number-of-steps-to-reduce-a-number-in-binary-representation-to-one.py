class Solution:
    def numSteps(self, s: str) -> int:
        n, tally = int(s,2), 0

        while n!= 1:
            if n&1:
                n+=1
            else:
                n>>=1
            tally+=1
        return tally
        
        #bNumb = int(s, 2)
        #print(bNumb)
        #stepCount = 0
        #while bNumb > 1:
            #if bNumb % 2 == 0:
                #bNumb /= 2
                #stepCount+=1
            #else:
                #bNumb += 1
                #stepCount+=1
        #return stepCount
            