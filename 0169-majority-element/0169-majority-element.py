class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = Counter(nums)
        return max(count, key=count.get)