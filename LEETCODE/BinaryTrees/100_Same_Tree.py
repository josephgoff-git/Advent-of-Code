# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def construct_tree(arr):
#     if not arr:
#         return None

#     root = TreeNode(arr[0])
#     queue = [root]
#     i = 1

#     while i < len(arr):
#         current = queue.pop(0)

#         if arr[i] is not None:
#             current.left = TreeNode(arr[i])
#             queue.append(current.left)

#         i += 1

#         if i < len(arr) and arr[i] is not None:
#             current.right = TreeNode(arr[i])
#             queue.append(current.right)

#         i += 1

#     return root



# class Solution:
#     def isSameTree(self, p, q):
#         if not p and not q:
#             return True
#         elif not p or not q:
#             return False
#         else:
#             return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
# sol = Solution()
# tree1 = [1, None, 2]
# tree2 = [1, None, 2]
# tree3 = [1, None, 2, 3]

# tree1_ = construct_tree(tree1)
# tree2_ = construct_tree(tree2)
# tree3_ = construct_tree(tree3)

# print(sol.isSameTree(tree1_, tree2_)) 
# print(sol.isSameTree(tree2_, tree3_)) 




class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructTree(array):
    if not array:
        return None

    i = 1
    root = TreeNode(array[0])
    queue = [root]

    while i < len(array):
        current = queue.pop(0)
        if current is not None:
            queue.append(current.left)
            