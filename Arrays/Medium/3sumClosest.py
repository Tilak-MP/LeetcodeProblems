nums = [-1,2,1,-4]
target = 1

class solution:
  def threeSumClosest(self,nums,target):
    nums.sort()
    result = nums[0] + nums[1] + nums[2]

    for i in range(len(nums)-2):
      l, r = i+1, len(nums)-1
      while l < r:
        total = nums[i] + nums[l] + nums[r]

        if abs(target - total) < abs(target - result):
          result = total

        if result == target:
          return target
        elif result < target:
          l += 1
        else: 
          r -= 1

    return result

s = solution()
result = s.threeSumClosest(nums,target)
print(result)