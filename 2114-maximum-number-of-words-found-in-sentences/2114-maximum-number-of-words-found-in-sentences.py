class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        maxSentance = 0
        for i in sentences:
            space = 0
            for j in i:
                if j == ' ':
                    space=space+1
            maxSentance=max(maxSentance, space+1)
        return maxSentance