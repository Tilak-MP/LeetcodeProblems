class solution:
  def containsDuplicate(self,nums):
    # map = {}
    # for i in nums:
    #   if i in map:
    #     return True
    #   else:
    #     map[i] = i

    # return False

    s = set(nums)

    if len(s) == len(nums):
      return False
    
    return True

# nums = [1,2,3,1]
# nums = [1,1,1,3,3,4,3,2,4,2]
nums = [1,2,3,1]
s = solution()
result = s.containsDuplicate(nums)
print(result)