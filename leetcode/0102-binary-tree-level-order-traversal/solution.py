# 102. Binary Tree Level Order Traversal
# 難度：Medium 🟡
# 題型：Tree, Breadth-First Search
# 本程式提供一個二元樹的層序遍歷解法，並包含測試範例與詳細註解

from collections import deque  # 匯入 deque 以便進行 BFS


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val              # 節點值
        self.left = left            # 左子節點
        self.right = right          # 右子節點

# 層序遍歷主函式
# root: TreeNode，二元樹的根節點
# 回傳：List[List[int]]，每層節點值的列表


def levelOrder(root):
    result = []                    # 儲存最終結果
    if not root:
        return result              # 若樹為空，直接回傳空列表
    queue = deque([root])          # 初始化佇列，將根節點放入
    while queue:                   # 當佇列不為空時
        level = []                 # 儲存當前層的節點值
        for _ in range(len(queue)):
            node = queue.popleft()  # 取出佇列最左側節點
            level.append(node.val)  # 加入當前層結果
            if node.left:
                queue.append(node.left)   # 若有左子節點，加入佇列
            if node.right:
                queue.append(node.right)  # 若有右子節點，加入佇列
        result.append(level)              # 將本層結果加入最終結果
    return result


# 範例測試
if __name__ == "__main__":
    # 建立如下二元樹：
    #     3
    #    / \
    #   9  20
    #      /  \
    #     15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(levelOrder(root))  # 預期輸出：[[3], [9, 20], [15, 7]]
