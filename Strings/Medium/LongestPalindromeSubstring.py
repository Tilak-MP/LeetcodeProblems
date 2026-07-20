class solution:
  def longestPalindromeSubstring(self,s):
    if not s or len(s) < 1:
      return ""
    
    start, end = 0, 0

    def expand_around_center(l, r):

      while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1

      return r - l - 1
    
  
    for i in range(len(s)):
      
      len1 = expand_around_center(i,i)

      len2 = expand_around_center(i,i+1)

      max_len = max(len1,len2)

      if max_len > (end - start):
        start = i - (max_len - 1) // 2
        end = i + max_len // 2

    return s[start:end+1]

s = "babad"
result = solution().longestPalindromeSubstring(s)
print(result)