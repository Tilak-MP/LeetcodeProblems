strs = ["flower","flow","flight"]

class solution():
  def LongestCommonPrefix(self,strs):
    # if not strs:
    #   return ""
    # res = ""
    # for a in zip(*strs):
    #   if len(set(a)) == 1:
    #     res += a[0]
    #   else:
    #     return res
    # return res

    ans = ""
    strs = sorted(strs)
    f, l = strs[0], strs[-1]
    for i in range(min(len(f),len(l))):
      if f[i] != l[i]:
        return ans
      ans += f[i]

    return ans

s = solution()
result = s.LongestCommonPrefix(strs)
print(result)