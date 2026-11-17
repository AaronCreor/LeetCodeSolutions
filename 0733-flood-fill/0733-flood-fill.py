class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        starting = image[sr][sc]
        stack = [(sr, sc)]
        while stack:
            r, c = stack.pop()
            image[r][c] = color
            if r > 0:
                if image[r-1][c] == starting and image[r-1][c] != color:
                    stack.append((r-1, c))
            if r < len(image)-1:
                if image[r+1][c] == starting and image[r+1][c] != color:
                    stack.append((r+1, c))
            if c > 0:
                if image[r][c-1] == starting and image[r][c-1] != color:
                    stack.append((r, c-1))
            if c < len(image[0])-1:
                if image[r][c+1] == starting and image[r][c+1] != color:
                    stack.append((r, c+1))
        return image
