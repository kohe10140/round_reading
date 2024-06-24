from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:

    def __init__(self, root=None):
        self.root = root

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            queue = deque()
            queue.append(self.root)
            while len(queue) > 0:
                node = queue.popleft()
                if node.left is not None:
                    queue.append(node.left)
                else:
                    node.left = TreeNode(val)
                    break
                if node.right is not None:
                    queue.append(node.right)
                else:
                    node.right = TreeNode(val)
                    break

    def search(self, val):
        if self.root is None:
            return False
        queue = deque()
        queue.append(self.root)
        while len(queue) > 0:
            node = queue.popleft()
            if node.val == val:
                return True
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return False

    def delete(self, val):
        return
    
    def getRandomNode(self):
        return