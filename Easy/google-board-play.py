'''
You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.
Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.
For example, given the following board:
[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
'''
# Use BFS where visit all adjacent position of current position
def bfs(board, start, end):
    visited = list()
    queue = list()

    queue.append((start, 0))
    while queue:
        pos, dist = queue.pop(0)
        if pos == end:
            return dist
        
        for adj_pos in get_adjacents(pos, board):
            if adj_pos not in visited:
                visited.append(adj_pos)
                queue.append((adj_pos, dist + 1))
    return None

def get_adjacents(currentPosition, board):
    adjacents = list() # List of adjacents positions of the current position
    n = len(board) - 1
    m = len(board[currentPosition[1]]) - 1

    if currentPosition[0] < n: # Down?
        if board[currentPosition[0] + 1][currentPosition[1]] == False:
            adjacents.append([currentPosition[0] + 1, currentPosition[1]])
    if currentPosition[0] > 0: # Up?
        if board[currentPosition[0] - 1][currentPosition[1]] == False:
            adjacents.append([currentPosition[0] - 1, currentPosition[1]])
    if currentPosition[1] > 0: # Left?
        if board[currentPosition[0]][currentPosition[1] - 1] == False:
            adjacents.append([currentPosition[0], currentPosition[1] - 1])
    if currentPosition[1] < m: # Right?
        if board[currentPosition[0]][currentPosition[1] + 1] == False:
            adjacents.append([currentPosition[0], currentPosition[1] + 1])
    return adjacents

boardTest = [
    [False, False, False, False],
    [True, True, False, True],
    [False, False, False, False],
    [False, False, False, False]
]
start = [3, 0]
end = [0, 0]
minSteps = 7
assert bfs(boardTest, start, end) == minSteps

# Complexity Analysis
# Time complexity: 
#    - Worst case: visit all paths: O(m * n)
#    - Average case: visit some points: O(m * n)
#    - Best case: start = end: O(1)