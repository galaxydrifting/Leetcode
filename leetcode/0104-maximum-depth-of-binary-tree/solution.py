# 定義二元樹節點類別
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val              # 節點值
        self.left = left            # 左子節點
        self.right = right          # 右子節點

# 主解法類別


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        遞迴 DFS 解法
        """
        if not root:               # 若節點為空，回傳 0
            return 0
        # 遞迴計算左右子樹最大深度，取最大值再加 1
        left_depth = self.maxDepth(root.left)   # 左子樹深度
        right_depth = self.maxDepth(root.right)  # 右子樹深度
        return max(left_depth, right_depth) + 1  # 最大深度

    def maxDepth_bfs(self, root: TreeNode) -> int:
        """
        BFS（層序遍歷）解法
        """
        if not root:
            return 0
        from collections import deque            # 匯入 deque 作為 queue
        queue = deque([root])                   # 初始化 queue，放入根節點
        depth = 0                               # 初始化深度
        while queue:                            # 當 queue 不為空
            level_size = len(queue)             # 當前層節點數
            for _ in range(level_size):         # 遍歷當前層所有節點
                node = queue.popleft()          # 彈出節點
                if node.left:
                    queue.append(node.left)     # 左子節點入 queue
                if node.right:
                    queue.append(node.right)    # 右子節點入 queue
            depth += 1                          # 每層結束深度+1
        return depth

    def maxDepth_iterative_dfs(self, root: TreeNode) -> int:
        """
        迭代 DFS（使用 stack）解法
        """
        if not root:
            return 0
        stack = [(root, 1)]                     # stack 存 (節點, 當前深度)
        max_depth = 0                           # 初始化最大深度
        while stack:
            node, depth = stack.pop()           # 彈出節點與深度
            if node:
                max_depth = max(max_depth, depth)  # 更新最大深度
                if node.left:
                    stack.append((node.left, depth + 1))  # 左子節點入 stack
                if node.right:
                    stack.append((node.right, depth + 1))  # 右子節點入 stack
        return max_depth


# 範例測試
if __name__ == "__main__":
    # 建立範例樹 root = [3,9,20,null,null,15,7]
    root = TreeNode(3)                 # 建立根節點 3
    root.left = TreeNode(9)            # 左子節點 9
    root.right = TreeNode(20)          # 右子節點 20
    root.right.left = TreeNode(15)     # 右子節點的左子節點 15
    root.right.right = TreeNode(7)     # 右子節點的右子節點 7
    sol = Solution()                   # 建立 Solution 物件
    print(sol.maxDepth(root))          # 輸出: 3
    print(sol.maxDepth_bfs(root))      # 輸出: 3
    print(sol.maxDepth_iterative_dfs(root))  # 輸出: 3

    # 另一個範例 root = [1, None, 2]
    root2 = TreeNode(1)                # 建立根節點 1
    root2.right = TreeNode(2)          # 右子節點 2
    print(sol.maxDepth(root2))         # 輸出: 2
    print(sol.maxDepth_bfs(root2))     # 輸出: 2
    print(sol.maxDepth_iterative_dfs(root2))  # 輸出: 2
