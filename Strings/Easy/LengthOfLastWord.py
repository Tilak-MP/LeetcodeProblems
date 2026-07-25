class solution:
  def lengthOfLastWord(self,s):
    s = s.strip()
    if s == "":
      return 0
    for i in range(len(s)-1,-1,-1):
      if s[i] == " ":
        return len(s[i+1:])

    return len(s)

# s = "   fly me   to   the moon  "
# s = "Hello World"
s = "luffy is still joyboy"
result = solution().lengthOfLastWord(s)
print(result)