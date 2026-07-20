class solution:
  def firstAccurance(self,str,s):
  
    for i in range(len(str)-len(s)+1):
      if s == str[i:i+len(s)]:
        return i
      
    return -1

haystack = "sadbutsad"
needle = "sad"
s = solution()
result = s.firstAccurance(haystack,needle)
print(result)