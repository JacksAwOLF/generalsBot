import heapq
import math

# position  - tuple storing 0-indexed general postion (row, col) 
# grid      - grid storing map; 1 if the cell is passable
# length    - the desired length of the path
#
# returns the reversed path as a list of tuples if found; -1 otherwise
def get_path_to_middle(position, grid, length):
    center = (len(grid)/2, len(grid[0])/2)
    if center == position:
        center[0] += 1

    # find difference vector and scale it
    diff = (center[0]-position[0], center[1]-position[1])
    mag = math.sqrt(diff[0] ** 2 + diff[1] ** 2)

    target = (center[0] + diff[0] / mag * 15, center[1] + diff[1] / mag * 15)

    # heuristic distance function
    def h(pos):
        return math.sqrt((pos[0] - target[0]) ** 2 + (pos[1] - target[1]) ** 2)

    cameFrom = dict()
    gScore = dict()
    fScore = dict()

    cameFrom[position] = -1
    gScore[position] = 0
    fScore[position] = h(position)

    pq = [(-fScore[position], position)]
    moves = [[0,1],[1,0],[-1,0],[0,-1]]

    while len(pq) > 0:
        f, cur = heappop(pq)

        if gScore[cur] == length:
            path = []
            while cur != -1:
                path.append(cur)
                cur = cameFrom[cur]
            
            return path
        
        for i in range(4):
            nxt = (cur[0]+moves[i][0], cur[1]+moves[i][1])
            if nxt[0] >= len(grid) or nxt[0] < 0 or nxt[1] >= len(grid[0]) or nxt[1] < 0:
                continue
            elif grid[nxt[0]][nxt[1]] and gScore[cur] + 1 < gScore.get(nxt, 1000):
                gScore[nxt] = gScore[cur] + 1
                fScore[nxt] = gScore[nxt] + h(nxt)
                cameFrom[nxt] = cur

                heappush(pq, (-fScore[nxt], nxt))
    
    return -1


