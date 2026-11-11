class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if costBoth <= min(cost1, cost2):
            return costBoth * max(need1, need2)
        elif costBoth < cost1 and costBoth > cost2:
            total = costBoth*need1
            total += cost2*(max(0,(need2-need1)))
            return total
        elif costBoth > cost1 and costBoth < cost2:
            total = costBoth*need2
            total += cost1*(max(0,(need1 - need2)))
            return total
        else:
            totBoth = min(need1, need2)
            totBothCost = totBoth * costBoth
            remain1 = need1 - min(need1, need2)
            remain2 = need2 - min(need1, need2)
            totBothCost = totBothCost + ((remain1 * cost1) + (remain2 * cost2))
            return min(totBothCost, ((cost1*need1)+(cost2*need2)))
