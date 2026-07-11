nums = [1,2,3]
target = 2

# class solution:
#   def searchRange(self,nums,target):

#     l, r = 0, len(nums)-1
#     i, j = -1, -1

#     if r == 0:
#       if nums[l] == target:
#         return [l,r] 

#     while l <= r:

#       print(l,r)

#       if nums[l] == target:
#         i = l
#       if nums[r] == target:
#         j = r

#       if i == -1 and j == -1:
#         l += 1
#         r -= 1
#       elif i > -1 and j == -1:
#         r -= 1
#       elif i == -1 and j > -1:
#         l += 1
#       else:
#         return [i,j]

#     if i > -1 and j == -1:
#       return [i,i]
#     elif i == -1 and j > -1:
#       return [j,j]
#     else:
#       return [i,j]

class solution:
    def searchRange(self, nums, target):
        def findBound(isFirst):
            low, high = 0, len(nums) - 1
            bound = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    bound = mid
                    if isFirst:
                        high = mid - 1
                    else:
                        low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return bound
        return [findBound(True), findBound(False)]

s = solution()
result = s.searchRange(nums,target)
print(result)