# 110. Balanced Binary Tree

> 難度：Easy 🟢

> 題型：Tree, DFS, Recursion

## 題目描述
> Given a binary tree, determine if it is height-balanced.
> 
> For this problem, a height-balanced binary tree is defined as:
> a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
>
> 給定一個二元樹，判斷它是否為高度平衡的二元樹。
> 
> 高度平衡的二元樹定義為：
> 對於這棵樹的每個節點，其左右子樹的高度差不超過 1。

---

## 💡 解題思路
1. 使用遞迴（DFS）自底向上計算每個節點的高度。
2. 若發現某個子樹不平衡，則直接返回 False。
3. 若所有節點都平衡，則返回 True。

> ⚠️ 可以在計算高度的同時檢查平衡性，避免重複遍歷。

---

## 📚 範例

| 輸入 | 輸出 |
|------|------|
| root = [3,9,20,null,null,15,7] | True |
| root = [1,2,2,3,3,null,null,4,4] | False |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                |
|--------------|---------------------|
| 使用資料結構 | 二元樹、遞迴         |
| 時間複雜度   | O(n)                |
| 空間複雜度   | O(h)，h 為樹高       |
| 優點         | 一次遍歷即可判斷     |
| 缺點         | 需理解遞迴與樹高計算 |

---

## 🧑‍💻 程式碼（Python，含註解）

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # 定義遞迴函數，回傳 [是否平衡, 樹高]
        def dfs(node) -> [bool, int]:
            if not node:
                return [True, 0]  # 空節點視為平衡，高度為 0
            left = dfs(node.left)  # 遞迴處理左子樹
            right = dfs(node.right)  # 遞迴處理右子樹
            # 當前節點平衡需左右子樹都平衡且高度差不超過 1
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]  # 回傳平衡狀態與高度
        return dfs(root)[0]  # 只需回傳是否平衡
```
