class Solution(object):
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)
                else:
                    empty_cells.append((r, c))
        def backtrack(empty_idx):
            if empty_idx == len(empty_cells):
                return True
            r, c = empty_cells[empty_idx]
            box_idx = (r // 3) * 3 + (c // 3)
            for d in ["1","2","3","4","5","6","7","8","9"]:
                if d not in rows[r] and d not in cols[c] and d not in boxes[box_idx]:
                    board[r][c] = d
                    rows[r].add(d)
                    cols[c].add(d)
                    boxes[box_idx].add(d)
                    if backtrack(empty_idx + 1):
                        return True
                    board[r][c] = '.'
                    rows[r].remove(d)
                    cols[c].remove(d)
                    boxes[box_idx].remove(d)
            return False
        backtrack(0)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna