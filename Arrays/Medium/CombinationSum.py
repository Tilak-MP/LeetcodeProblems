class solution:
  def combinationSum(self,arr,target):

    result = []
    arr.sort()

    def backtrack(remain,start,path):

      if remain == 0:
        result.append(list(path))
        return
      
      for i in range(start,len(arr)):

        if arr[i] > remain:
          break

        path.append(arr[i])

        backtrack(remain-arr[i],i,path)

        path.pop()
      
    backtrack(target,0,[])

    return result
  
candidates = [2,3,5]
target = 8
s = solution()
result = s.combinationSum(candidates,target)
print(result)