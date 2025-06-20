# 100. Same Tree

> 難度：Easy 🟢

> 題型：Tree, DFS, Recursion

## 題目描述
> 給定兩棵二元樹的根節點 `p` 和 `q`，請寫一個函數來判斷這兩棵樹是否相同。
> 
> 兩棵二元樹被認為是相同的，當且僅當它們在結構上完全相同，且對應節點的值也相等。

> Given the roots of two binary trees p and q, write a function to check if they are the same or not.
> 
> Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

---

## 💡 解題思路
1. 若兩個節點皆為空，則相同。
2. 若其中一個節點為空，或值不同，則不同。
3. 遞迴比較左右子樹。

---

## 📚 範例

| 輸入 | 輸出 |
|------|------|
| p = [1,2,3], q = [1,2,3] | True |
| p = [1,2], q = [1,null,2] | False |
| p = [1,2,1], q = [1,1,2] | False |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                |
|--------------|---------------------|
| 使用資料結構 | 二元樹、遞迴         |
| 時間複雜度   | O(N)                |
| 空間複雜度   | O(N)（遞迴棧最壞情況）|
| 優點         | 實作簡單、易於理解   |
| 缺點         | 遞迴深度受限於樹高   |

---

## 🧑‍💻 程式碼（Python）

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # 節點值
        self.left = left  # 左子樹
        self.right = right  # 右子樹

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    # 若兩節點皆為空，則相同
    if not p and not q:
        return True
    # 若其中一個為空或值不同，則不同
    if not p or not q or p.val != q.val:
        return False
    # 遞迴比較左右子樹
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
```
