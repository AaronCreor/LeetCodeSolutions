class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        mult = 1
        val = 0
        while len(columnTitle) > 0:
            val += ((ord(columnTitle[-1])-64)*mult)
            mult=mult*26
            columnTitle = columnTitle[:-1]
        return val