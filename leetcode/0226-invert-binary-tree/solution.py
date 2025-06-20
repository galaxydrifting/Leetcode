# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val              # 節點值
        self.left = left            # 左子樹
        self.right = right          # 右子樹

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:               # 若樹為空，直接回傳 None
            return None
        # 交換左右子樹
        root.left, root.right = root.right, root.left
        # 遞迴反轉左子樹
        self.invertTree(root.left)
        # 遞迴反轉右子樹
        self.invertTree(root.right)
        return root                # 回傳反轉後的根節點

# 範例測試
if __name__ == "__main__":
    def build_tree(nodes):
        # 由陣列建立二元樹（BFS）
        if not nodes:
            return None
        from collections import deque
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

    def tree_to_list(root):
        # 將二元樹轉為陣列（BFS）
        from collections import deque
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        # 移除尾端多餘的 None
        while result and result[-1] is None:
            result.pop()
        return result

    # 測試用例
    test_cases = [
        [4,2,7,1,3,6,9],
        [2,1,3],
        []
    ]
    for case in test_cases:
        root = build_tree(case)                 # 建立原始樹
        inv = Solution().invertTree(root)       # 反轉樹
        print(tree_to_list(inv))                # 輸出反轉後的陣列
