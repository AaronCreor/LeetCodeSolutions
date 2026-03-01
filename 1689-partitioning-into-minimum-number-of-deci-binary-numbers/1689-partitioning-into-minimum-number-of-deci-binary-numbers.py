class Solution:
    def minPartitions(self, n: str) -> int:
        nList = list(n)
        ret = 0
        for i in range(len(nList)):
            ret = max(ret, int(nList[i]))
        return ret
