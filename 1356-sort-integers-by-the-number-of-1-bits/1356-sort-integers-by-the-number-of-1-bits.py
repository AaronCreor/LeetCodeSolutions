class Solution:
    def countBits(self, x):#return bitcount
        c = 0
        while x > 0:
            if x & 1:
                c+=1
            x >>= 1
        return c
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda x: (self.countBits(x), x))
        return arr
        