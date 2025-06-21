# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # 節點值
        self.left = left  # 左子節點
        self.right = right  # 右子節點


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')  # 初始化最大路徑和為負無窮

        def dfs(node):
            if not node:
                return 0  # 空節點貢獻為 0
            # 遞迴計算左子樹最大貢獻，若小於 0 則視為 0
            left_gain = max(dfs(node.left), 0)
            # 遞迴計算右子樹最大貢獻，若小於 0 則視為 0
            right_gain = max(dfs(node.right), 0)
            # 經過當前節點的最大路徑和
            current_sum = node.val + left_gain + right_gain
            # 更新全域最大路徑和
            self.max_sum = max(self.max_sum, current_sum)
            # 回傳給父節點的最大貢獻（只能選一邊）
            return node.val + max(left_gain, right_gain)

        dfs(root)  # 從 root 開始 DFS
        return self.max_sum  # 回傳最大路徑和


# 範例測試
if __name__ == "__main__":
    # 範例 1: root = [1,2,3]
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    print(Solution().maxPathSum(root1))  # 輸出: 6

    # 範例 2: root = [-10,9,20,null,null,15,7]
    root2 = TreeNode(-10)
    root2.left = TreeNode(9)
    root2.right = TreeNode(20)
    root2.right.left = TreeNode(15)
    root2.right.right = TreeNode(7)
    print(Solution().maxPathSum(root2))  # 輸出: 42
