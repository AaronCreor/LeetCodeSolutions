class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        altMax = 0
        for i in range(0, len(gain), 1):
            alt += gain[i]
            altMax = (max(alt, altMax))
        return altMax