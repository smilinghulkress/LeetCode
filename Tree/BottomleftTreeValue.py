class Tree(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r

def findLeftMostNode(root):
    queue = [root]
    for node in queue:
        # queue += filter(None, (node.right, node.left))
        queue += filter(lambda node: node != None, [node.right, node.left])
    return node.val

b = Tree(7, None, None)
a = Tree(15, None, None)
left = Tree(9, None, None)
right = Tree(20, a, b)
root = Tree(3, left, right)

print(findLeftMostNode(root))