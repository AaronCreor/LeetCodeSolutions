class Solution:
    def judgeCircle(self, moves: str) -> bool:
        Y = 0
        X = 0
        for i in moves:
            if i == 'U':
                Y=Y+1
            elif i == 'D':
                Y=Y-1
            elif i == 'L':
                X=X-1
            else:
                X=X+1
        if Y == 0 and X == 0:
            return True
        else:
            return False