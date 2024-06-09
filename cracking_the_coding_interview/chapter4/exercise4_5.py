from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        pass

    def isValidBST(self, root) -> bool:
        VAL_MIN = -2 ** 31 -1
        VAL_MAX = 2 ** 31
        return self._isValid(root, VAL_MIN, VAL_MAX)
    
    def _isValid(self, node, floor, cap):
        if node is None:
            return None
        if floor < node.val < cap:
            l = self._isValid(node.left, floor, node.val)
            if l == False:
                return False
            r = self._isValid(node.right, node.val, cap)
            if r == False:
                return False
        else:
            return False
        return True

s = Solution()
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
print(s.isValidBST(root))

s = Solution()
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(s.isValidBST(root))