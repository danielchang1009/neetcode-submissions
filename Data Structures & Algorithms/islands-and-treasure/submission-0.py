class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col  = len(grid) ,len(grid[0])
        q = deque()
        visited = set()
        def addcell(r,c):
            if (min(r,c)<0 or r == row or c == col or (r,c) in visited or grid[r][c] == -1 ):
                return 
            q.append([r,c])
            visited.add((r,c))
        for r in range(row):
            for c in range(col):
                if grid [r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))
        dist = 0 
        while q :
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                addcell(r+1,c)
                addcell(r-1,c) 
                addcell(r,c+1) 
                addcell(r,c-1) 
            dist+=1



