# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # 節點值
        self.left = left  # 左子樹
        self.right = right  # 右子樹


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 定義遞迴函式，帶入上下界
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True  # 空節點視為合法
            if node.val <= lower or node.val >= upper:
                return False  # 違反 BST 條件
            # 遞迴檢查左子樹與右子樹
            return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)
        return helper(root)


# 範例測試
if __name__ == "__main__":
    # 範例 1: root = [2,1,3]
    root1 = TreeNode(2)  # 建立根節點 2
    root1.left = TreeNode(1)  # 左子節點 1
    root1.right = TreeNode(3)  # 右子節點 3
    print(Solution().isValidBST(root1))  # 預期輸出 True

    # 範例 2: root = [5,1,4,null,null,3,6]
    root2 = TreeNode(5)  # 建立根節點 5
    root2.left = TreeNode(1)  # 左子節點 1
    root2.right = TreeNode(4)  # 右子節點 4
    root2.right.left = TreeNode(3)  # 右子節點的左子節點 3
    root2.right.right = TreeNode(6)  # 右子節點的右子節點 6
    print(Solution().isValidBST(root2))  # 預期輸出 False
