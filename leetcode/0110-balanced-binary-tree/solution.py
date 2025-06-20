# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional


class Solution:
    def isBalanced(self, root: Optional['TreeNode']) -> bool:
        # 定義遞迴函數，回傳 [是否平衡, 樹高]
        def dfs(node) -> list:
            if not node:
                return [True, 0]  # 空節點視為平衡，高度為 0
            left = dfs(node.left)  # 遞迴處理左子樹
            right = dfs(node.right)  # 遞迴處理右子樹
            # 當前節點平衡需左右子樹都平衡且高度差不超過 1
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]  # 回傳平衡狀態與高度
        return dfs(root)[0]  # 只需回傳是否平衡


# 範例測試
if __name__ == "__main__":
    # 範例一：root = [3,9,20,null,null,15,7]
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    print(Solution().isBalanced(root1))  # 輸出 True

    # 範例二：root = [1,2,2,3,3,null,null,4,4]
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(3)
    root2.left.left.left = TreeNode(4)
    root2.left.left.right = TreeNode(4)
    print(Solution().isBalanced(root2))  # 輸出 False
