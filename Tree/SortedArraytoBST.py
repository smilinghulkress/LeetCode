class Tree(object):
    def __init__(self, x, l = None, r = None):
        self.val = x
        self.left = l
        self.right = r

class Solution(object):
    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None
        mid = len(nums)//2
        root = Tree(nums[mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        root.left = self.sortedArrayToBST(nums[0:mid])
        return root



input = [-10,-3,0,5,9]
sol = Solution()
print(sol.sortedArrayToBST(input).right.val)