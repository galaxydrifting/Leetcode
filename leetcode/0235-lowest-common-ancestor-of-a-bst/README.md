# 235. Lowest Common Ancestor of a Binary Search Tree

> 難度：Medium 🟡

> 題型：Tree, Binary Search Tree

## 題目描述
> 給定一棵二元搜尋樹（BST），找出給定兩個節點 p 和 q 的最近共同祖先（LCA）。
>
> 根據維基百科對於最近共同祖先的定義：「在一棵樹 T 中，節點 p 和 q 的最近共同祖先是同時擁有 p 和 q 作為後代（可以包含自身）的最低節點。」
>
> Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
>
> According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

---

## 💡 解題思路
1. 由於是 BST，左子樹所有值小於根節點，右子樹所有值大於根節點。
2. 從根節點開始遍歷：
   - 若 p 和 q 都小於當前節點，則 LCA 在左子樹。
   - 若 p 和 q 都大於當前節點，則 LCA 在右子樹。
   - 否則，當前節點即為 LCA。
3. 只需一路往下搜尋，直到分叉點即為答案。

> ⚠️ 注意：BST 性質讓我們可以不用回溯，直接自頂向下找到分叉點。

---

## 📚 範例

| 輸入 | 輸出 |
|------|------|
| root = [6,2,8,0,4,7,9,none,none,3,5], p = 2, q = 8 | 6 |
| root = [6,2,8,0,4,7,9,none,none,3,5], p = 2, q = 4 | 2 |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                |
|--------------|---------------------|
| 使用資料結構 | 二元搜尋樹（BST）   |
| 時間複雜度   | O(h)，h 為樹高      |
| 空間複雜度   | O(1)（遞迴則 O(h)） |
| 優點         | 善用 BST 性質，效率高|
| 缺點         | 需理解 BST 結構      |

---

## 🧑‍💻 程式碼（Python，含註解）

```python
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
```
