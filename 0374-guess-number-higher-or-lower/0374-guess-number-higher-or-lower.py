# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        guessNum = (right // 2)+1
        for _ in (range(0, n, 1)):
            print(guessNum)
            if(guess(guessNum) == 0):
                return guessNum
            elif(guess(guessNum) == 1):
                left = guessNum+1
                guessNum = (left+right)//2
            else:
                right = guessNum-1
                guessNum = (left+right)//2
            