# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # 節點值
        self.left = left  # 左子樹
        self.right = right  # 右子樹


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # 定義遞迴函數，帶入目前節點與路徑最大值
        def dfs(node, max_val):
            if not node:
                return 0  # 空節點不計算
            # 若當前節點值大於等於路徑最大值，則為好節點
            good = 1 if node.val >= max_val else 0
            # 更新最大值
            max_val = max(max_val, node.val)
            # 遞迴左右子樹
            good += dfs(node.left, max_val)
            good += dfs(node.right, max_val)
            return good
        return dfs(root, root.val)  # 從根節點開始，最大值為根值


# 範例測試用例
if __name__ == "__main__":
    # Helper function: 由 list 建立二元樹
    def build_tree(nodes):
        from collections import deque
        if not nodes:
            return None
        root = TreeNode(nodes[0])
        queue = deque([root])
        i = 1
        while queue and i < len(nodes):
            node = queue.popleft()
            if nodes[i] is not None:
                node.left = TreeNode(nodes[i])
                queue.append(node.left)
            i += 1
            if i < len(nodes) and nodes[i] is not None:
                node.right = TreeNode(nodes[i])
                queue.append(node.right)
            i += 1
        return root

    # 測試 1
    root1 = build_tree([3, 1, 4, 3, None, 1, 5])
    print(Solution().goodNodes(root1))  # 輸出: 4

    # 測試 2
    root2 = build_tree([3, 3, None, 4, 2])
    print(Solution().goodNodes(root2))  # 輸出: 3

    # 測試 3
    root3 = build_tree([1])
    print(Solution().goodNodes(root3))  # 輸出: 1
