# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # 節點值
        self.left = left  # 左子節點
        self.right = right  # 右子節點


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_diameter = 0  # 初始化最大直徑

        def dfs(node):
            if not node:
                return 0  # 空節點深度為 0
            left_depth = dfs(node.left)  # 遞迴獲取左子樹深度
            right_depth = dfs(node.right)  # 遞迴獲取右子樹深度
            # 更新最大直徑（左深度 + 右深度）
            self.max_diameter = max(
                self.max_diameter, left_depth + right_depth)
            return max(left_depth, right_depth) + 1  # 回傳該節點的最大深度

        dfs(root)  # 從根節點開始 DFS
        return self.max_diameter  # 回傳最大直徑


# 範例測試
if __name__ == "__main__":
    # 建立範例二元樹 root = [1,2,3,4,5]
    root = TreeNode(1)  # 建立根節點 1
    root.left = TreeNode(2)  # 左子節點 2
    root.right = TreeNode(3)  # 右子節點 3
    root.left.left = TreeNode(4)  # 2 的左子節點 4
    root.left.right = TreeNode(5)  # 2 的右子節點 5
    sol = Solution()  # 建立 Solution 物件
    print(sol.diameterOfBinaryTree(root))  # 輸出 3，代表最長路徑長度為 3
