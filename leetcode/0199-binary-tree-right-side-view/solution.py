# Definition for a binary tree node.
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # 節點值
        self.left = left  # 左子節點
        self.right = right  # 右子節點


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    result = []  # 用來存放右視圖節點值
    if not root:
        return result  # 若樹為空，直接回傳空列表
    queue = deque([root])  # 初始化佇列，放入根節點
    while queue:
        level_size = len(queue)  # 當前層的節點數
        for i in range(level_size):
            node = queue.popleft()  # 取出當前層的節點
            if node.left:
                queue.append(node.left)  # 左子節點加入佇列
            if node.right:
                queue.append(node.right)  # 右子節點加入佇列
            if i == level_size - 1:
                result.append(node.val)  # 最右邊的節點加入結果
    return result  # 回傳右視圖


# 範例測試
if __name__ == "__main__":
    # 建立範例樹 root = [1,2,3,null,5,null,4]
    root = TreeNode(1)  # 建立根節點 1
    root.left = TreeNode(2)  # 左子節點 2
    root.right = TreeNode(3)  # 右子節點 3
    root.left.right = TreeNode(5)  # 2 的右子節點 5
    root.right.right = TreeNode(4)  # 3 的右子節點 4
    print(rightSideView(root))  # 輸出: [1, 3, 4]
