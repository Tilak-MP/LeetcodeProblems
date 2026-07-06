nums = [2,7,11,15]
target = 9

class solution(object):
  def twosum(self, nums, target):
    map = {}
    for i, num in enumerate(nums):
      if target - num in map:
        return [map[target - num], i]
      map[num] = i

    return
  
result = solution()
print(result.twosum(nums, target))