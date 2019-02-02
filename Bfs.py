from collections import deque

num_row = 0
num_col = 0
obstacles = []
#East, south, west, north
moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def find_next_point(curr, r_diff, c_diff):
    r, c = curr
    if (c_diff != 0):
        while (True):
            next = c + c_diff
            if (next < 0 or next == num_col or obstacles[r][next] == 1):
                break
            else:
                c = next
    if (r_diff != 0):
        while (True):
            next = r + r_diff
            if (next < 0 or next >= num_row or obstacles[next][c] == 1):
                break
            else:
                r = next
    return (r, c)

def initialize_visited():
    global visited
    visited = []
    for i in range(num_row):
        row = []
        for j in range(num_col):
            row.append(False)
        visited.append(row)

def minimum_steps(obst, start, end):
    q = deque() # It can be used as queue or stack
    global num_row, num_col, obstacles
    obstacles = obst
    num_row = len(obst)
    num_col = len(obst[0])

    initialize_visited()
    q.append((start, 0)) # step is the level of BFS,  assuming start is level 0
    visited[start[0]][start[1]] = True
    # I need to record level info. I cannot use processing counter as step since points are flattened in queue
    while (q):
        curr, level = q.popleft()
        for move in moves:
            next = find_next_point(curr, move[0], move[1])
            if (next == end):
                return level + 1 #step = curr level + 1,
            # Optimize
            if (not visited[next[0]][next[1]]):
                q.append((next, level+1))
                visited[next[0]][next[1]] = True

if __name__ == '__main__':
    obst = [
        [0, 0, 0, 1],
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0]
    ]

    start = (1, 1)
    end = (3, 3)
    print("Case 1: Minimum steps = %d" % minimum_steps(obst, start, end))

    obst = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0]
    ]

    start = (1, 1)
    end = (7, 7)
    print("Case 2: Minimum steps = %d" % minimum_steps(obst, start, end))