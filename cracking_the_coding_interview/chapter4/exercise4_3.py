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

    def levelOrder(self, root):
        if root is None:
            return []
        result = []
        queue = deque([root])
        layer = deque([0])
        # layerのqueueを作成せずとも，parentsのListを作成すれば良い
        while len(queue) != 0:
            node = queue.popleft()
            l = layer.popleft()
            if len(result) <= l:
                result.append([])
            result[l].append(node.val)

            if node.left is not None:
                queue.append(node.left)
                layer.append(l+1)
            if node.right is not None:
                queue.append(node.right)
                layer.append(l+1)
        return result

s = Solution()
