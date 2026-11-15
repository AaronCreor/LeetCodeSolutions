class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapify(maxHeap)
        while maxHeap:
            stone = heappop(maxHeap)
            if len(maxHeap) == 0:
                return abs(stone)
            stone = stone - heappop(maxHeap)
            if stone != 0:
                heappush(maxHeap, stone)
        return abs(stone)


