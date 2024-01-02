def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]
    
    orig_color = image[sr][sc]
    stack = []
    stack.append((sr, sc))
    while len(stack) > 0:
        s = stack.pop()
        visited[s[0]][s[1]] = True
        image[s[0]][s[1]] = color
        if s[0] > 0 and not visited[s[0] - 1][s[1]] and image[s[0] - 1][s[1]] == orig_color:
            stack.append((s[0] - 1, s[1]))
        if s[0] < len(image) - 1 and not visited[s[0] + 1][s[1]] and image[s[0] + 1][s[1]] == orig_color:
            stack.append((s[0] + 1, s[1]))
        if s[1] > 0 and not visited[s[0]][s[1] - 1] and image[s[0]][s[1] - 1] == orig_color:
            stack.append((s[0], s[1] - 1))
        if s[1] < len(image[0]) - 1 and not visited[s[0]][s[1] + 1] and image[s[0]][s[1] + 1] == orig_color:
            stack.append((s[0], s[1] + 1))
    
    return image