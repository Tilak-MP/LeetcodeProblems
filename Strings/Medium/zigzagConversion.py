class solution:
  def zigzagConversion(self,s,rows):

    if rows <= 0:
      return ""
    elif rows == 1:
      return s

    map = {i:"" for i in range(rows)}
    n = rows + (rows-2)
    row = 0
    for i in range(len(s)):
      if i % n >= rows:
        row -= 1
      else:
        row = i%n
      map[row] += s[i]

    return "".join(map.values())

# s = "PAYPALISHIRING"
s = "A"
numRows = 4
result = solution().zigzagConversion(s,numRows)
print(result)