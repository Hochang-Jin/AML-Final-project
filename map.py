import numpy as np
import random

def mapMaker(a=10, b=10, n_walls=0):
    while True:
        map = np.zeros((a,b), dtype=int)
        for i in range(a):
            for j in range(b):
                if i == 0 or j == 0 or i == a-1 or j == b-1:
                    map[i][j] = 3
        x, y = random.randint(1,a-2), random.randint(1,b-2)

        map[x][y] = 1

        while map[x][y] == 1 or map[x][y] == 3:
            x, y = random.randint(1, a-2), random.randint(1, b-2)

        map[x][y] = 2

        for i in range(n_walls):
            while map[x][y] == 1 or map[x][y] == 2 or map[x][y] == 3:
                x, y = random.randint(1, a-2), random.randint(1, b-2)
            map[x][y] = 3
        print(minDistance(map))
        if minDistance(map) > -1:
            break


    return map


# Python3 Code implementation for above problem

# QItem for current location and distance
# from source location
class QItem:
    def __init__(self, row, col, dist):
        self.row = row
        self.col = col
        self.dist = dist

    def __repr__(self):
        return f"QItem({self.row}, {self.col}, {self.dist})"


def minDistance(grid):
    source = QItem(0, 0, 0)
    grid = grid.tolist()
    # Finding the source to start from
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                source.row = row
                source.col = col
                break

    # To maintain location visit status
    visited = [[False for _ in range(len(grid[0]))]
               for _ in range(len(grid))]

    # applying BFS on matrix cells starting from source
    queue = []
    queue.append(source)
    visited[source.row][source.col] = True
    while len(queue) != 0:
        source = queue.pop(0)

        # Destination found;
        if (grid[source.row][source.col] == 2):
            return source.dist

        # moving up
        if isValid(source.row - 1, source.col, grid, visited):
            queue.append(QItem(source.row - 1, source.col, source.dist + 1))
            visited[source.row - 1][source.col] = True

        # moving down
        if isValid(source.row + 1, source.col, grid, visited):
            queue.append(QItem(source.row + 1, source.col, source.dist + 1))
            visited[source.row + 1][source.col] = True

        # moving left
        if isValid(source.row, source.col - 1, grid, visited):
            queue.append(QItem(source.row, source.col - 1, source.dist + 1))
            visited[source.row][source.col - 1] = True

        # moving right
        if isValid(source.row, source.col + 1, grid, visited):
            queue.append(QItem(source.row, source.col + 1, source.dist + 1))
            visited[source.row][source.col + 1] = True

    return -1


# checking where move is valid or not
def isValid(x, y, grid, visited):
    if ((x >= 0 and y >= 0) and
            (x < len(grid) and y < len(grid[0])) and
            (grid[x][y] != 3) and (visited[x][y] == False)):
        return True
    return False


# This code is contributed by sajalmittaldei.




