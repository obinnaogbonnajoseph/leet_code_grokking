class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        if not board or not board[0]:
            return 0

        rows, cols = len(board), len(board[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'X':
                    # Check if it's the start of a battleship
                    is_top_x = (r == 0 or board[r-1][c] == '.')
                    is_left_x = (c == 0 or board[r][c-1] == '.')
                    
                    if is_top_x and is_left_x:
                        count += 1
                        
        return count
