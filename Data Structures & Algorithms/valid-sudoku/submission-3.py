class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxs = defaultdict(set)
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if not num.isdigit():
                    continue

                box_coord = (r // 3, c // 3)
                if num not in (rows[r] | cols[c] | boxs[box_coord]):
                    rows[r].add(num)
                    cols[c].add(num)
                    boxs[box_coord].add(num)
                else:
                    return False
        return True