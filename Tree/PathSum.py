
class Solution:
    def hasPathSum(self, root, sum):
        return self.preorder(root,sum,0)

    def preorder(self,root,sum,localsum):
        if not root:
            return False
        if not root.left and not root.right and localsum==sum:
            return True
        return self.preorder(root.left,sum,localsum+root.val) or self.preorder(root.right,sum,localsum+root.val)


