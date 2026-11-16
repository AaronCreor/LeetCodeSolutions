class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashMap = Counter(nums)

        heap = [(freq, num) for num, freq in hashMap.items()]
        heapify_max(heap)
        res = []
        for i in range(k):
            res.append(heappop_max(heap)[1])
        return res

