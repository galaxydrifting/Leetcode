# 572. Subtree of Another Tree

> 難度：Easy 🟢

> 題型：Tree

## 題目描述
> 給定兩個二元樹的根節點 `root` 和 `subRoot`，判斷 `subRoot` 是否為 `root` 的子樹。
> 
> A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

---

## 💡 解題思路
1. 針對 `root` 的每個節點，檢查以該節點為根的子樹是否與 `subRoot` 完全相同。
2. 若相同則回傳 True，否則遞迴檢查左右子樹。
3. 判斷兩棵樹是否相同可用遞迴：若當前節點值相同，且左右子樹也分別相同，則兩樹相同。

> ⚠️ 注意：空樹也是任何樹的子樹。

---

## 📚 範例

| 輸入 | 輸出 |
|------|------|
| root = [3,4,5,1,2], subRoot = [4,1,2] | True |
| root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2] | False |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                |
|--------------|---------------------|
| 使用資料結構 | 二元樹 (Binary Tree) |
| 時間複雜度   | O(m * n) (m, n 分別為兩樹節點數) |
| 空間複雜度   | O(h) (h 為主樹高度，遞迴棧空間) |
| 優點         | 直觀、易於實作      |
| 缺點         | 最壞情況下效率較低  |

---

## 🧑‍💻 程式碼（Python）

```python
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
```

---
