class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
            b_size = 3
            empty_value= '.'
            seen = set()
            size = b_size * b_size
            for row in range(size):
                for col in range(size):
                    if (value := board[row][col]) == empty_value:
                        continue
                    r = f'0{row}{value}'
                    c = f'1{col}{value}'
                    b = f'2{row // b_size}{col // b_size}{value}'
                    if r in seen or c in seen or b in seen:
                        return False
                    seen.update({r, c, b})
            return True
