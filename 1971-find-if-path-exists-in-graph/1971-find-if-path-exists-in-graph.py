class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen = {source}
        stack = [source]

        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for neighbour in graph[node]:
                if neighbour not in seen:
                    stack.append(neighbour)
                    seen.add(neighbour)
        return False


        