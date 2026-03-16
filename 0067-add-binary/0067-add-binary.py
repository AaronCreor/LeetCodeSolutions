class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aNum = int(a, 2)
        bNum = int(b, 2)
        cNum = aNum + bNum
        return bin(cNum)[2:]