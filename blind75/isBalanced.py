class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root: Optional[TreeNode]) -> bool:
    def helper(root):
        l_bal = r_bal = True
        l_h = r_h = 0
        if root == None:
            return 0, True
        if root.left:
            l_h, l_bal = helper(root.left)
        if root.right:
            r_h, r_bal = helper(root.right)
        
        if abs(r_h - l_h) <= 1 and r_bal and l_bal:
            return max(r_h, l_h) + 1, True
        else:
            return 0, False

    if root == None:
        return True
    h_r, bal_r = helper(root.right)
    h_l, bal_l = helper(root.left)
    if abs(h_r - h_l) <= 1 and bal_r and bal_l:
        return True
    else:
        return False