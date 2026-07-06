height = [1,8,6,2,5,4,8,3,7]

class solution():
  def maxArea(self,height):
    print(height)

    l, r = 0, len(height) - 1
    area = 0

    while l < r:
      area = max(area, min(height[l], height[r]) * (r-l))
      if height[l] < height[r]:
        l += 1
      else:
        r -= 1

    return area

result = solution()
print(result.maxArea(height))