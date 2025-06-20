# 102. Binary Tree Level Order Traversal

> 難度：Medium 🟡

> 題型：Tree & Breadth-First Search

## 題目描述
> 給定一個二元樹的根節點，請你回傳其節點值的「層序遍歷」結果（即逐層、從左到右）。

> Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

---

## 💡 解題思路
1. 若樹為空，直接回傳空列表。
2. 使用佇列（queue）進行廣度優先搜尋（BFS），將根節點放入佇列。
3. 每次迴圈處理一層：
   - 取出當前層所有節點，記錄其值。
   - 若有左右子節點，依序加入佇列。
4. 重複直到佇列為空。

> ⚠️ 注意：每層需單獨收集節點值，最後回傳所有層的結果。

---

## 📚 範例

| 輸入                                   | 輸出                |
|----------------------------------------|---------------------|
| root = [3,9,20,null,null,15,7]         | [[3], [9, 20], [15, 7]] |
| root = []                             | []                  |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                        |
|--------------|-----------------------------|
| 使用資料結構 | 佇列（queue）、二元樹         |
| 時間複雜度   | O(n)，n 為節點數             |
| 空間複雜度   | O(n)，最壞情況需存放所有節點   |
| 優點         | 能完整逐層遍歷所有節點        |
| 缺點         | 額外空間需求較 DFS 多         |

---

## 🧑‍💻 程式碼（Python，含詳細中文註解）

```python
from collections import deque  # 匯入 deque 以便進行 BFS

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val              # 節點值
        self.left = left            # 左子節點
        self.right = right          # 右子節點

def levelOrder(root):
    result = []                    # 儲存最終結果
    if not root:
        return result              # 若樹為空，直接回傳空列表
    queue = deque([root])          # 初始化佇列，將根節點放入
    while queue:                   # 當佇列不為空時
        level = []                 # 儲存當前層的節點值
        for _ in range(len(queue)):
            node = queue.popleft() # 取出佇列最左側節點
            level.append(node.val) # 加入當前層結果
            if node.left:
                queue.append(node.left)   # 若有左子節點，加入佇列
            if node.right:
                queue.append(node.right)  # 若有右子節點，加入佇列
        result.append(level)              # 將本層結果加入最終結果
    return result

# 範例測試
if __name__ == "__main__":
    # 建立如下二元樹：
    #     3
    #    / \
    #   9  20
    #      /  \
    #     15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(levelOrder(root))  # 預期輸出：[[3], [9, 20], [15, 7]]
```

---
