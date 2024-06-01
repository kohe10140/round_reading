import math
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._rec_insert(self.root, val)
    
    def _rec_insert(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._rec_insert(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._rec_insert(node.right, val)


def sortedArrayToBST(nums: list[int]):
    return create_sub_tree(nums, 0, len(nums)-1)

def create_sub_tree(nums, start, end):
    # リストそのものでなく，Indexを渡した方が良い場合もある
    # 今回は境界の処理が簡単なためIndexを使う方が良い
    if start > end:
        return None
    mid = int((start+end)/2)
    node = TreeNode(nums[mid])
    node.left = create_sub_tree(nums, start, mid-1)
    node.right = create_sub_tree(nums, mid+1, end)
    return node

print(sortedArrayToBST([-10,-3,0,5,9]))
print(sortedArrayToBST([1,3]))
print(sortedArrayToBST([3]))
