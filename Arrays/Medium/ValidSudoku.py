class solution:
  def validSudoku(self,board):

    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    # print(rows)

    for r in range(9):
      for c in range(9):

        num = board[r][c]

        if num == ".":
          continue

        box = ( r // 3 ) * 3 + ( c // 3 )

        if num in rows[r] or num in cols[c] or num in boxes[box]:
          return False
        
        rows[r].add(num)
        cols[c].add(num)
        boxes[box].add(num)

    return True

board = [
["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

s = solution()
result = s.validSudoku(board)
print(result)