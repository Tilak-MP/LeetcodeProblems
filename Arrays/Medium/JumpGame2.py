class solution:
  def jumpGame2(self,nums):
    jump, end, far = 0, 0, 0
    for i in range(len(nums)-1):
      far = max(far,i+nums[i])
      if i == end:
        jump += 1
        end = far
    return jump
                                                                                                                                   
nums = [2,3,1,1,4]
s = solution()
result = s.jumpGame2(nums)
print(result)