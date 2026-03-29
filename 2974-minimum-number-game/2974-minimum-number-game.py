class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        nums = sorted(nums, reverse=True)
        while len(nums) > 0:
            alice = nums.pop()
            bob = nums.pop()
            arr.append(bob)
            arr.append(alice)
        return arr