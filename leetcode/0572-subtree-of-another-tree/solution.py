# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # 節點值
        self.left = left  # 左子樹
        self.right = right  # 右子樹


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # 若 subRoot 為空，則必為子樹
        if not subRoot:
            return True  # 空樹是任何樹的子樹
        # 若 root 為空，subRoot 不為空，則不可能
        if not root:
            return False
        # 若當前節點相同，則檢查兩棵樹是否完全相同
        if self.isSameTree(root, subRoot):
            return True
        # 否則遞迴檢查左右子樹
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, s: TreeNode, t: TreeNode) -> bool:
        # 若兩者皆為空，則相同
        if not s and not t:
            return True
        # 若其中一者為空，則不同
        if not s or not t:
            return False
        # 若值不同，則不同
        if s.val != t.val:
            return False
        # 遞迴檢查左右子樹
        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)


# 範例測試用例
if __name__ == "__main__":
    # 建立主樹 root: [3,4,5,1,2]
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)

    # 建立子樹 subRoot: [4,1,2]
    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)

    # 建立 Solution 物件
    sol = Solution()
    # 執行並輸出結果
    print(sol.isSubtree(root, subRoot))  # 預期輸出: True

    # 另一組測試
    root2 = TreeNode(3)
    root2.left = TreeNode(4)
    root2.right = TreeNode(5)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(2)
    root2.left.right.left = TreeNode(0)
    subRoot2 = TreeNode(4)
    subRoot2.left = TreeNode(1)
    subRoot2.right = TreeNode(2)
    print(sol.isSubtree(root2, subRoot2))  # 預期輸出: False
