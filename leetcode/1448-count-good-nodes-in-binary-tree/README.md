# 1448. Count Good Nodes in Binary Tree

> 難度：Medium 🟡

> 題型：Tree, DFS, Binary Tree

## 題目描述
> 給定一棵二元樹 root，若某個節點 X 在從 root 到 X 的路徑上，沒有任何節點的值大於 X，則稱 X 為「好節點」。
> 
> 請回傳這棵樹中「好節點」的數量。
>
> Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
>
> Return the number of good nodes in the binary tree.

---

## 💡 解題思路
1. 使用 DFS（深度優先搜尋）遍歷整棵樹。
2. 在遞迴過程中，記錄從 root 到當前節點路徑上的最大值。
3. 若當前節點值大於等於路徑上的最大值，則該節點為好節點，計數加一。
4. 遞迴處理左右子樹，並更新最大值。

> ⚠️ 注意：根節點一定是好節點。

---

## 📚 範例

| 輸入 | 輸出 |
|------|------|
| root = [3,1,4,3,null,1,5] | 4 |
| root = [3,3,null,4,2]      | 3 |
| root = [1]                 | 1 |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                |
|--------------|---------------------|
| 使用資料結構 | 二元樹、遞迴         |
| 時間複雜度   | O(n)，n 為節點數     |
| 空間複雜度   | O(h)，h 為樹高（遞迴棧）|
| 優點         | 實作簡單、易於理解   |
| 缺點         | 遞迴深度過深時有棧溢出風險 |

---

## 🧑‍💻 Python 程式碼

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # 節點值
        self.left = left  # 左子樹
        self.right = right  # 右子樹

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # 定義遞迴函數，帶入目前節點與路徑最大值
        def dfs(node, max_val):
            if not node:
                return 0  # 空節點不計算
            # 若當前節點值大於等於路徑最大值，則為好節點
            good = 1 if node.val >= max_val else 0
            # 更新最大值
            max_val = max(max_val, node.val)
            # 遞迴左右子樹
            good += dfs(node.left, max_val)
            good += dfs(node.right, max_val)
            return good
        return dfs(root, root.val)  # 從根節點開始，最大值為根值
```
