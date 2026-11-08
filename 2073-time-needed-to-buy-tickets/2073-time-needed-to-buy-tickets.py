class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        count = 0
        while tickets[k] >= 1:
            for i in range(len(tickets)):
                if tickets[i] >= 1:
                    count=count+1
                    tickets[i] = tickets[i]-1
                if tickets[k] == 0:
                    return count
