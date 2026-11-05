class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        m = 0
        for i in range(len(arr1)):
            n = len(arr2)
            z = 0
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j]) > d:
                    z=z+1
                if z == n:
                    m=m+1
        return m