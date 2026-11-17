class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        seen = set()
        matrix = defaultdict(list)

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    matrix[i].append(j)
        
        def dfs(root):
            for node in matrix[root]:
                if node not in seen:
                    seen.add(node)
                    dfs(node)

        for node in matrix:
            if node not in seen:
                seen.add(node)
                dfs(node)
                provinces+=1
        return provinces
