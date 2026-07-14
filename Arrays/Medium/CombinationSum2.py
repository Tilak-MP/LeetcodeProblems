class solution:
  def combinationSum2(self,candidates,target):
    
    result = []
    candidates.sort()

    def backtrack(remain,start,path):
      if remain == 0:
        result.append(list(path))
        return
      
      for i in range(start,len(candidates)):

        if candidates[i] > remain:
          break

        if i > start and candidates[i] == candidates[i-1]:
          continue

        path.append(candidates[i])

        backtrack(remain-candidates[i],i+1,path)

        path.pop()

    backtrack(target,0,[])

    return result
  
# candidates = [1, 1, 2, 5]
# target = 8
candidates = [10,1,2,7,6,1,5]
target = 8
s = solution()
result = s.combinationSum2(candidates,target)
print(result)