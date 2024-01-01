class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root == None:
        return None
    
    return TreeNode(root.val, invertTree(root.right), invertTree(root.left))
