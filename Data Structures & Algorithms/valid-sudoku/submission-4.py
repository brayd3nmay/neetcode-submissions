class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                digit = board[i][j]
                if digit == ".":
                    continue
                elif digit in rows[i] or digit in cols[j] or digit in boxes[i // 3, j // 3]:
                    return False
                else:
                    rows[i].add(digit)
                    cols[j].add(digit)
                    boxes[i // 3, j // 3].add(digit)
        return True