# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # 節點值
        self.left = left  # 左子樹
        self.right = right  # 右子樹


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.count = 0  # 計數器，記錄已遍歷節點數
        self.result = None  # 存放第 k 小的值

        def inorder(node):
            if not node:
                return  # 遞迴終止條件
            inorder(node.left)  # 遍歷左子樹
            self.count += 1  # 計數器加一
            if self.count == k:
                self.result = node.val  # 找到第 k 小
                return
            inorder(node.right)  # 遍歷右子樹
        inorder(root)  # 從根節點開始中序遍歷
        return self.result  # 回傳結果


# 範例測試
if __name__ == "__main__":
    # 建立測試用 BST: [3,1,4,null,2]
    root = TreeNode(3)  # 建立根節點 3
    root.left = TreeNode(1)  # 左子節點 1
    root.right = TreeNode(4)  # 右子節點 4
    root.left.right = TreeNode(2)  # 1 的右子節點 2
    k = 1  # 取第 1 小
    print(Solution().kthSmallest(root, k))  # 輸出 1

    # 建立測試用 BST: [5,3,6,2,4,null,null,1]
    root2 = TreeNode(5)  # 根節點 5
    root2.left = TreeNode(3)  # 左子節點 3
    root2.right = TreeNode(6)  # 右子節點 6
    root2.left.left = TreeNode(2)  # 3 的左子節點 2
    root2.left.right = TreeNode(4)  # 3 的右子節點 4
    root2.left.left.left = TreeNode(1)  # 2 的左子節點 1
    k2 = 3  # 取第 3 小
    print(Solution().kthSmallest(root2, k2))  # 輸出 3
