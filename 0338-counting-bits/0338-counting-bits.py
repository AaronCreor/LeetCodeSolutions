class Solution:
    def countBits(self, n: int) -> List[int]:
        response = []
        for i in range(n+1):
            temp = i
            count = 0
            while i > 0:
                if (i & 1 == 1):
                    count=count+1
                    i = i >> 1
                else:
                    i = i >> 1
            response.append(count)
        return response