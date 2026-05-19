class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r, a in enumerate(board):
            for c, n in enumerate(a):
                if n.isdigit():
                    # populate row
                    if n not in rows[r]:
                        rows[r].add(n)
                    else:
                        return False 
                    # populate column
                    if n not in columns[c]:
                        columns[c].add(n)
                    else:
                        return False

                    # populate box
                    """
                    012
                    345
                    678
                    """
                    box = (r // 3 * 3) + c // 3
                    if n not in boxes[box]:
                        boxes[box].add(n)
                    else:
                        return False
            
        return True