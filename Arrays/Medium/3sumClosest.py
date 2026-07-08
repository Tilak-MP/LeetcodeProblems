nums = [-1,2,1,-4]
target = 1

class solution:
    def threeSumClosest(self, nums, target) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(target - total) < abs(target - result):
                    result = total

                if total == target:
                    return target
                elif total < target:
                    left += 1
                else:
                    right -= 1

        return result

s = solution()
result = s.threeSumClosest(nums,target)
print(result)