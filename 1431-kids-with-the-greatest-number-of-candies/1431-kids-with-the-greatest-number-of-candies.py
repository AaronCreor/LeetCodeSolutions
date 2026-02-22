class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        topCandies = max(candies)
        resultList = []
        for i in range(len(candies)):
            if((candies[i]+extraCandies)>=topCandies):
                resultList.append(True)
            else:
                resultList.append(False)
        return resultList