class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        majority = len(nums) // 2
        count = Counter(nums)
        return max(count, key=count.get)