class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        visited = set()
        max_area = 0

        def bfs(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            area = 1
            while q:
                row, col = q.popleft()
                directions = [[0,1],[1,0],[-1,0],[0,-1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if ( r in range(rows) and c in range(cols) and grid[r][c] == 1 and ((r,c)) not in visited):
                        q.append((r,c))
                        visited.add((r,c))
                        area += 1
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = bfs(r,c)
                    max_area = max(max_area, area)

        return max_area