class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        maxHeap = score.copy()
        heapify_max(maxHeap)
        count = 1
        while maxHeap:
            local = heappop_max(maxHeap)
            for i in range(len(score)):
                if score[i] == local:
                    if count == 1:
                        score[i] = "Gold Medal"
                        count+=1
                    elif count == 2:
                        score[i] = "Silver Medal"
                        count+=1
                    elif count == 3:
                        score[i] = "Bronze Medal"
                        count+=1
                    else:
                        score[i] = str(count)
                        count+=1
        return(score)
