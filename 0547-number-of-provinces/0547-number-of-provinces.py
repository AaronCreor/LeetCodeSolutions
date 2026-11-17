class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            visited.add(i)
            for j in range(n):
                if j not in visited and isConnected[i][j] == 1:
                    dfs(j)




        visited = set()
        n = len(isConnected)
        components = 0
        for i in range(n): # 0 to n
            if i not in visited:
                dfs(i)
                components += 1
        return components



