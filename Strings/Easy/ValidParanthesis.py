class solution:
  def validParanthesis(self,s):

    if len(s)<=1:
      return False

    mapping = {")": "(", "}": "{", "]": "["}
    arr = []

    for i in range(len(s)):

      if s[i] not in mapping:
        arr.append(s[i])
      else:
        if arr and mapping[s[i]] == arr[-1]:
          arr.pop()
        else:
          return False
    
    return arr == []

# str = "([])"
# str = "()[]{}"
# str = "()"
# str = "]"
str = "){"
s = solution()
result = s.validParanthesis(str)
print(result)