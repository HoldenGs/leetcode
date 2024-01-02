class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val > p.val and root.val > q.val:
            return lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return lowestCommonAncestor(root.right, p, q)
        else:
            return root