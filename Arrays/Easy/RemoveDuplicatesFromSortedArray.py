nums = [0,0,1,1,1,2,2,3,3,4]

class solution:
  def removeDuplicates(self,nums):

    if not nums:
      return 0
    
    l = 0

    for i in range(len(nums)):
      if nums[i] != nums[l]:
        l += 1
        nums[i], nums[l] = nums[l], nums[i]

    return l+1

s = solution()
result = s.removeDuplicates(nums)
print(result)