# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # 節點值
        self.left = left  # 左子樹
        self.right = right  # 右子樹


def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    # 若兩節點皆為空，則相同
    if not p and not q:
        return True  # 兩棵樹都為空，視為相同
    # 若其中一個為空或值不同，則不同
    if not p or not q or p.val != q.val:
        return False  # 只要有一棵樹為空或值不同，則不同
    # 遞迴比較左右子樹
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


# 範例測試
if __name__ == "__main__":
    # 建立範例樹 p = [1,2,3]
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    # 建立範例樹 q = [1,2,3]
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)

    # 測試相同樹
    print(isSameTree(p, q))  # 輸出 True

    # 建立範例樹 p2 = [1,2]
    p2 = TreeNode(1)
    p2.left = TreeNode(2)

    # 建立範例樹 q2 = [1,None,2]
    q2 = TreeNode(1)
    q2.right = TreeNode(2)

    # 測試不同結構
    print(isSameTree(p2, q2))  # 輸出 False

    # 建立範例樹 p3 = [1,2,1]
    p3 = TreeNode(1)
    p3.left = TreeNode(2)
    p3.right = TreeNode(1)

    # 建立範例樹 q3 = [1,1,2]
    q3 = TreeNode(1)
    q3.left = TreeNode(1)
    q3.right = TreeNode(2)

    # 測試值不同
    print(isSameTree(p3, q3))  # 輸出 False
