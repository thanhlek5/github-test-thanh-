# from typing import Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if not root:
#             return root
#         self.invertTree(root.right)
#         self.invertTree(root.left)
#         root.right,root.left = root.left,root.ringt
#         return root
# root = TreeNode()
# a=[4,2,7,1,3,6,9]
# print(root.invertTree(a))
# trời má bài tập đệ quy khó vãi lồn thế 

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root

# Hàm để xây dựng cây nhị phân từ danh sách
def insert_level_order(arr, root, i, n):
    if i < n:
        temp = TreeNode(arr[i])
        root = temp

        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    return root

# Hàm để in cây theo chiều sâu
def print_tree(node):
    if not node:
        return
    print(node.val, end=' ')
    print_tree(node.left)
    print_tree(node.right)

# Tạo cây nhị phân từ danh sách
a = [4, 2, 7, 1, 3, 6, 9]
root = insert_level_order(a, None, 0, len(a))

# Đảo ngược cây
solution = Solution()
inverted_root = solution.invertTree(root)

# In cây đã đảo ngược
print_tree(inverted_root)

