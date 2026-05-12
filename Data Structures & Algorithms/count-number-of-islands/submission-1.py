class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        visit = set()
        lslands = 0

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visit.add((r,c))
            while q:
                row, col = q.popleft()
                for dr,dc in directions:
                    nr, nc = dr+row, dc + col
                    if (nr not in range(rows) or nc not in range(cols) or grid[nr][nc] == "0" or (nr,nc) in visit):
                        continue
                    q.append((nr,nc))
                    visit.add((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    lslands += 1


        return lslands

