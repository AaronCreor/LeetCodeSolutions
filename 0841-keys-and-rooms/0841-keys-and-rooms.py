class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = set()
        stack = [0]


        
        while stack:
            room = stack.pop()
            if room not in visited:
                visited.add(room)
                for i in range(len(rooms[room])):

                    stack.append(rooms[room][i])
        
        if len(visited) == len(rooms):
            return True
        else:
            return False

