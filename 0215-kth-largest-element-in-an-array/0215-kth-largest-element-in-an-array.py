class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapify_max(nums)
        i = 1
        val = 0
        while i <= k:
            val = heappop_max(nums)
            i=i+1
        return val

            
        