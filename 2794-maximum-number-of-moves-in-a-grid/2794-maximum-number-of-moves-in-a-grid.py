
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        memo = {}

        def dfs(row, col):
            if col == cols - 1:
                return 0
            
            if (row, col) in memo:
                return memo[(row, col)]
            
            max_moves = 0
            current_val = grid[row][col]
        
            for dr, dc in [(-1, 1), (0, 1), (1, 1)]:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and new_col < cols and grid[new_row][new_col] > current_val:
                    max_moves = max(max_moves, 1 + dfs(new_row, new_col))
            
            memo[(row, col)] = max_moves
            return max_moves

        max_result = max(dfs(row, 0) for row in range(rows))
        return max_result
