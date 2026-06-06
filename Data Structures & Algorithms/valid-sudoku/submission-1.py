class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_set = [set() for _ in range(9)]
        cols_set = [set() for _ in range(9)]
        boxes_set = [set() for _ in range(9)]

        for i in range(0, 9):
            for j in range(0, 9):
                el = board[i][j]
                box = i // 3 * 3 + j // 3
                if el == '.':
                    continue
                if el in rows_set[i] or el in cols_set[j] or el in boxes_set[box]:
                    return False
                rows_set[i].add(el)
                cols_set[j].add(el)
                boxes_set[box].add(el)
        return True
