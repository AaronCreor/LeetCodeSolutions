class Solution:
    def arraySign(self, nums: list[int]) -> int:
        


        def signFunc(product):
            if product > 0:
                return 1
            elif product < 0:
                return -1
            else:
                return 0

        return signFunc(prod(nums))