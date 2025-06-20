# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val              # 節點值
        self.left = left            # 左子樹
        self.right = right          # 右子樹


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 只要 root 不為空
        while root:
            # 如果 p 和 q 都小於 root，往左子樹找
            if p.val < root.val and q.val < root.val:
                root = root.left
            # 如果 p 和 q 都大於 root，往右子樹找
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                # 否則 root 就是最近共同祖先
                return root
        return None  # 若未找到，回傳 None


# 範例測試
if __name__ == "__main__":
    # 建立測試用 BST
    n0 = TreeNode(0)
    n3 = TreeNode(3)
    n5 = TreeNode(5)
    n4 = TreeNode(4, n3, n5)
    n2 = TreeNode(2, n0, n4)
    n7 = TreeNode(7)
    n9 = TreeNode(9)
    n8 = TreeNode(8, n7, n9)
    root = TreeNode(6, n2, n8)

    p = n2  # 節點 2
    q = n8  # 節點 8
    sol = Solution()
    lca = sol.lowestCommonAncestor(root, p, q)
    print(f"LCA of {p.val} and {q.val} is {lca.val}")  # 應輸出 6

    p = n2  # 節點 2
    q = n4  # 節點 4
    lca = sol.lowestCommonAncestor(root, p, q)
    print(f"LCA of {p.val} and {q.val} is {lca.val}")  # 應輸出 2
