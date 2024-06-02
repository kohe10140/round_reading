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

    def isBalanced(self, root):
        if root is None:
            return True
        if not self._isSubBalanced(root):
            return False
        current = [root]
        while len(current) != 0:
            parents = current
            current = []
            for parent in parents:
                if parent.left is not None:
                    current.append(parent.left)
                    if not self._isSubBalanced(parent.left):
                        return False

                if parent.right is not None:
                    current.append(parent.right)
                    if not self._isSubBalanced(parent.right):
                        return False
        return True

    def _get_height(self, node):
        if node is None:
            return 0
        return max(self._get_height(node.left), self._get_height(node.right)) + 1

    def _isSubBalanced(self, node):
        return abs(self._get_height(node.left)-self._get_height(node.right)) < 2
        


s = Solution()

t1 = TreeNode(0)
print(s.isBalanced(t1))
t1.left = TreeNode(1)
print(s.isBalanced(t1))
t1.left.left = TreeNode(2)
print(s.isBalanced(t1))
t1.right = TreeNode(1)
print(s.isBalanced(t1))
t1.right.right = TreeNode(2)
t1.left.left.left = TreeNode(3)
t1.right.right.right = TreeNode(3)
print(s.isBalanced(t1))