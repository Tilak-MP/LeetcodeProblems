nums = [0,1,2,2,3,0,4,2,4]
val = 2

class solution:
  def removeElement(self,nums,val):
    
    l = 0

    for i in range(len(nums)):
      if nums[i] != val:
        nums[l] = nums[i]
        l += 1

    return l


s = solution()
result = s.removeElement(nums,val)
print(result)