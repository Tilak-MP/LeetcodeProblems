from typing import List, Optional

class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

# class solution:
#     def sortedArrayToBST(self, nums):
#         if len(nums) == 0:
#             return None

#         mid = len(nums) // 2

#         root = TreeNode(nums[mid])

#         root.left = self.sortedArrayToBST(nums[:mid])

#         root.right = self.sortedArrayToBST(nums[mid+1:])

#         return root

class solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n=len(nums)
        if n==0:
            return None
        return self.fun( nums,0,n-1)

    def fun(self,arr,l,r):
        if l>r:
            return None

        mid=(l+r)//2
        node=TreeNode(arr[mid])
        node.left=self.fun(arr,l,mid-1)
        node.right=self.fun(arr,mid+1,r)

        return node


nums = [-10,-3,0,5,9]
s = solution()
result = s.sortedArrayToBST(nums)
print(result)