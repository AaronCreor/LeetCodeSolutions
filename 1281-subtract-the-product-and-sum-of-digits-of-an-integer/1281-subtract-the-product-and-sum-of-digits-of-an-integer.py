class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        sums = 0
        prod = 1
        for i in n:
            local = int(i)
            sums+=local
            prod*=local
        return prod-sums


        
