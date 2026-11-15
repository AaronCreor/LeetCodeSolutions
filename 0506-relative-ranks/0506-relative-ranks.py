class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        maxHeap = []
        for index, value in enumerate(score):
            heappush_max(maxHeap, (value, index))
        count = 1
        while maxHeap:
            index = heappop_max(maxHeap)[1]
            if count == 1:
                score[index] = "Gold Medal"
                count+=1
            elif count == 2:
                score[index] = "Silver Medal"
                count+=1
            elif count == 3:
                score[index] = "Bronze Medal"
                count+=1
            else:
                score[index] = str(count)
                count+=1
        return(score)
