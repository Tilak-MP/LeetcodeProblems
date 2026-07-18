class solution:
  def majorityElement(self,nums):
    # if not nums:
    #   return 0
    # map = {}
    # most = 0
    # res = 0
    # for i in nums:
    #   if i not in map:
    #     map[i] = 1
    #   else:
    #     map[i] += 1

    #   if map[i] > most:
    #     res = i
    #     most = map[i]
    
    # return res
    return sorted(nums)[len(nums)//2]
      
nums = [2,2,1,1,1,1,2]
# nums = [3,2,3]
s = solution()
result = s.majorityElement(nums)
print(result)