class solution:
  def permutation(self,nums):
    result = []
    def backtrack(first):
      if first == len(nums):
        result.append(nums[:])
        return
      for i in range(first,len(nums)):
        nums[first], nums[i] = nums[i], nums[first]
        backtrack(first+1)
        nums[first], nums[i] = nums[i], nums[first]
    backtrack(0)
    return result

nums = [1,2,3]
s = solution()
result = s.permutation(nums)
print(result)