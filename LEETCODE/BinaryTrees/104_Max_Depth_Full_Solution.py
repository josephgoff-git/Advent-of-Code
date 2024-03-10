# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right) 

        return 1 + max(lh, rh)
    

sol = Solution()

# Example 1
tree1 = [3, 9, 20, None, None, 15, 7]

def construct_tree_from_array(arr):
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = [root]
    i = 1

    while i < len(arr):
        current = queue.pop(0)

        if arr[i] is not None:
            current.left = TreeNode(arr[i])
            queue.append(current.left)

        i += 1

        if i < len(arr) and arr[i] is not None:
            current.right = TreeNode(arr[i])
            queue.append(current.right)

        i += 1

    return root

tree1_root = construct_tree_from_array(tree1)
print(sol.maxDepth(tree1_root))  # Output: 3

# Example 2
tree2 = [1, None, 2]

tree2_root = construct_tree_from_array(tree2)
print(sol.maxDepth(tree2_root))  # Output: 2