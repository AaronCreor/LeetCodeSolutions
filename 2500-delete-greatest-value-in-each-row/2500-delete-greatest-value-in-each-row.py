class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        ans = 0
        local = 0
        while len(grid[0]) > 0:
            ans+=local
            local = 0
            for i in grid:
                heapify_max(i)
                local = max(local, heappop_max(i))
        ans+=local
        return ans