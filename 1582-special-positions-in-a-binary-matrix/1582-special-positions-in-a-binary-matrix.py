class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        m, n = len(mat), len(mat[0])

        for r, row in enumerate(mat):
            rCount = 0
            rP = -1

            for i in range(n):
                if row[i] == 1:
                    rCount += 1
                    rP = i
                    if rCount > 1:
                        break

            if rCount == 1:
                cCount = 0
                for rr in range(m):
                    if mat[rr][rP] == 1:
                        cCount += 1
                        if cCount > 1:
                            break

                if cCount == 1:
                    count += 1

        return count