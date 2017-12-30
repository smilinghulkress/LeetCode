from collections import deque
class Solution:
    def minDepth(self, root):
        q = deque()
        if not root:
            return 0
        q.append(root)
        depth = 1
        while q:
            flag = False
            k = len(q)
            for i in range(k):
                flag = True
                node = q.popleft()
                if not node.left and not node.right:
                    return depth+1
                else:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if flag == True:
                depth +=1
                flag = False
        return depth



