class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ret = []
        for i in matrix:
            count = 0
            for j in i:
                if j == 1:
                    count = count+1
            ret.append(count)
        return ret