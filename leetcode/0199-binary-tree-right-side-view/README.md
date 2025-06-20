# 199. Binary Tree Right Side View

> 難度：Medium 🟡

> 題型：Tree, Breadth-First Search, Depth-First Search

## 題目描述
> 給定一個二元樹的根節點 root，請你想像自己站在該樹的右側，返回從上到下所能看到的節點值。

> Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

---

## 💡 解題思路
1. 可以使用 BFS（廣度優先搜尋）逐層遍歷，每層只取最右邊的節點。
2. 也可以用 DFS（深度優先搜尋），優先遍歷右子樹，記錄每層第一次出現的節點。
3. 推薦 BFS，因為易於理解且直觀。

> ⚠️ 注意：若某層只有一個節點，則那個節點就是右視圖節點。

---

## 📚 範例

| 輸入 | 輸出 |
|------|------|
| root = [1,2,3,null,5,null,4] | [1,3,4] |
| root = [1,null,3] | [1,3] |
| root = [] | [] |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                        |
|--------------|-----------------------------|
| 使用資料結構 | Queue（佇列）、List（列表） |
| 時間複雜度   | O(n)                        |
| 空間複雜度   | O(n)                        |
| 優點         | 直觀、易於理解               |
| 缺點         | 需額外空間存放佇列           |

---

## 🧑‍💻 程式碼（Python，含註解）

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # 節點值
        self.left = left  # 左子節點
        self.right = right  # 右子節點

from typing import List, Optional
from collections import deque

def rightSideView(root: Optional[TreeNode]) -> List[int]:
    result = []  # 用來存放右視圖節點值
    if not root:
        return result  # 若樹為空，直接回傳空列表
    queue = deque([root])  # 初始化佇列，放入根節點
    while queue:
        level_size = len(queue)  # 當前層的節點數
        for i in range(level_size):
            node = queue.popleft()  # 取出當前層的節點
            if node.left:
                queue.append(node.left)  # 左子節點加入佇列
            if node.right:
                queue.append(node.right)  # 右子節點加入佇列
            if i == level_size - 1:
                result.append(node.val)  # 最右邊的節點加入結果
    return result  # 回傳右視圖

# 範例測試
if __name__ == "__main__":
    # 建立範例樹 root = [1,2,3,null,5,null,4]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    print(rightSideView(root))  # 輸出: [1, 3, 4]
```
---
