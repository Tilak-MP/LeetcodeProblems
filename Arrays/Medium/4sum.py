# nums = [1,0,-1,0,-2,2]
# target = 0

nums = [2,2,2,2,2]
target = 8

class solution:
    def fourSum(self, nums, target):
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                left = j + 1
                right = n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])

                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
        return ans

s = solution()
result = s.fourSum(nums, target)
print(result)