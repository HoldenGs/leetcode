from collections import deque

def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
    q, visited = get_zeros_and_visited(mat)

    while len(q) > 0:
        y, x = q.popleft()
        for yn, xn in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            yn = y + yn
            xn = x + xn
            if yn >= 0 and yn < len(mat) and xn >= 0 and xn < len(mat[0]) and not visited[yn][xn]:
                mat[yn][xn] = mat[y][x] + 1
                visited[yn][xn] = True
                q.append((yn, xn))

    return mat

def get_zeros_and_visited(mat: List[List[int]]):
    q = deque()
    visited = [[False for _ in range(len(mat[0]))] for _ in range(len(mat))]

    for y in range(len(mat)):
        for x in range(len(mat[0])):
            if mat[y][x] == 0:
                visited[y][x] = True
                q.append((y, x))

    return q, visited