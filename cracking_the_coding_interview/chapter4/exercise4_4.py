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

    def check(self, root):
        if root is None:
            return True
        none_depth = 1e+10
        current_depth = 0
        current = [root]
        while len(current) != 0:
            parents = current
            current = []
            #breakpoint()
            for parent in parents:
                if parent.left is not None:
                    current.append(parent.left)
                else:
                    none_depth = min(none_depth, current_depth+1)
                if parent.right is not None:
                    current.append(parent.right)
                else:
                    none_depth = min(none_depth, current_depth+1)
                if current_depth - none_depth > 0: # 最も浅いNoneの深さと最も深いノードの深さの差分が１より大きいとFalse
                    return False
            current_depth += 1
        return True


s = Solution()

t1 = TreeNode(0)
print(s.check(t1))
t1.left = TreeNode(1)
print(s.check(t1))
t1.left.left = TreeNode(2)
print(s.check(t1))
t1.right = TreeNode(1)
print(s.check(t1))
