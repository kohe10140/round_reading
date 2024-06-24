# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, targetSum: int) -> int:
        if root is None:
            return 0
        self.targetSum = targetSum
        _, cnt = self._get_subsum(root)
        return cnt
    
    def _get_subsum(self, node):
        subsum = [0] # 0 is val itself
        cnt = 0
        if node.left is not None:
            subsum_left, cntl = self._get_subsum(node.left)
            subsum += subsum_left
            cnt += cntl
        if node.right is not None:
            subsum_right, cntr = self._get_subsum(node.right)
            subsum += subsum_right
            cnt += cntr
        for i in range(len(subsum)):
            subsum[i] += node.val
            if subsum[i] == self.targetSum:
                cnt += 1
        return subsum, cnt