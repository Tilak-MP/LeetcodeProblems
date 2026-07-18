class solution:
  def singleNumber(self,nums):
    res = 0
    for i in nums:
      res ^= i
    return res

nums = [2,2,1,1,4]

s = solution()
result = s.singleNumber(nums)
print(result)