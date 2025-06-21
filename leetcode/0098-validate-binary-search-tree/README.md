# 98. Validate Binary Search Tree

> 難度：Medium 🟡

> 題型：Tree, DFS, Binary Search Tree

## 題目描述

給定一個二元樹的根節點 root，判斷其是否為有效的二元搜尋樹（BST）。

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

---

## 💡 解題思路
1. 使用遞迴（DFS）遍歷整棵樹。
2. 每個節點都必須滿足：其值大於左子樹所有節點且小於右子樹所有節點。
3. 透過傳遞上下界（min, max）來限制每個節點的合法值範圍。
4. 若有任何節點不符合 BST 條件，立即回傳 False。

> ⚠️ 注意：節點值必須嚴格小於右子樹、嚴格大於左子樹，不能等於。

---

## 📚 範例

| 輸入 | 輸出 |
|------|------|
| root = [2,1,3] | True |
| root = [5,1,4,null,null,3,6] | False |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                        |
|--------------|-----------------------------|
| 使用資料結構 | 二元樹、遞迴                |
| 時間複雜度   | O(n)                        |
| 空間複雜度   | O(h)，h 為樹的高度           |
| 優點         | 實作簡單、效率高             |
| 缺點         | 遞迴過深時可能導致堆疊溢位   |

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
    def isValidBST(self, root: TreeNode) -> bool:
        # 定義遞迴函式，帶入上下界
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True  # 空節點視為合法
            if node.val <= lower or node.val >= upper:
                return False  # 違反 BST 條件
            # 遞迴檢查左子樹與右子樹
            return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)
        return helper(root)
```
