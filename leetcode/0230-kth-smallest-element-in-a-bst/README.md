# 230. Kth Smallest Element in a BST

> 難度：Medium 🟡

> 題型：Binary Search Tree, Inorder Traversal

## 題目描述
給定一個二元搜尋樹（BST）的根節點 root 和一個整數 k，請你返回這棵樹中第 k 小的節點值（1-indexed）。

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

---

## 💡 解題思路
1. 利用 BST 的性質，中序遍歷（Inorder Traversal）可以得到遞增排序的節點值。
2. 進行中序遍歷，並用計數器記錄已經遍歷到第幾個節點。
3. 當計數器等於 k 時，回傳當前節點值。

> ⚠️ 注意：k 一定合法，且 BST 節點值皆唯一。

---

## 📚 範例

| 輸入 | 輸出 |
|------|------|
| root = [3,1,4,null,2], k = 1 | 1 |
| root = [5,3,6,2,4,null,null,1], k = 3 | 3 |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                |
|--------------|---------------------|
| 使用資料結構 | 二元搜尋樹（BST）   |
| 時間複雜度   | O(H + k)，H 為樹高  |
| 空間複雜度   | O(H)，遞迴棧空間    |
| 優點         | 利用 BST 性質高效搜尋|
| 缺點         | 需完整遍歷 k 個節點  |

---

## 🧑‍💻 程式碼（Python，含註解）

```python
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
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    k = 1
    print(Solution().kthSmallest(root, k))  # 輸出 1

    # 建立測試用 BST: [5,3,6,2,4,null,null,1]
    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.right = TreeNode(6)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(4)
    root2.left.left.left = TreeNode(1)
    k2 = 3
    print(Solution().kthSmallest(root2, k2))  # 輸出 3
```
