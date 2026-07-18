class solution:
    def permutations2(self, nums):
        output = []
        nums.sort()
        marked = [False] * len(nums)

        def allper(curr):
            if len(curr) == len(nums):
                output.append(curr.copy())
                return

            for i in range(len(nums)):
                if marked[i]:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and not marked[i - 1]:
                    continue

                marked[i] = True
                curr.append(nums[i])

                allper(curr)

                curr.pop()
                marked[i] = False

        allper([])
        return output

nums = [1,1,2]
s = solution()
result = s.permutations2(nums)
print(result)