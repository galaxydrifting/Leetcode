# 226. Invert Binary Tree

> 難度：Easy 🟢

> 題型：Tree, Binary Tree, DFS, BFS

## 題目描述
> Given the root of a binary tree, invert the tree, and return its root.
>
> 給定一個二元樹的根節點，請將這棵樹「反轉」，並回傳其根節點。

---

## 💡 解題思路
1. 遍歷每個節點，將其左右子樹交換。
2. 可以用遞迴（DFS）或迴圈（BFS）實現。
3. 遞迴：對每個節點，先交換左右子樹，再遞迴處理左右子樹。
4. 迴圈：用佇列層序遍歷，每次將節點左右子樹交換。

> ⚠️ 樹為空時直接回傳 None。

---

## 📚 範例

| 輸入 | 輸出 |
|------|------|
| root = [4,2,7,1,3,6,9] | [4,7,2,9,6,3,1] |
| root = [2,1,3] | [2,3,1] |
| root = [] | [] |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                |
|--------------|---------------------|
| 使用資料結構 | 二元樹、佇列（BFS） |
| 時間複雜度   | O(n)                |
| 空間複雜度   | O(n)（最壞遞迴深度或佇列大小） |
| 優點         | 實作簡單、易於理解  |
| 缺點         | 遞迴過深時有堆疊溢出風險 |

---

## 🧑‍💻 程式碼（Python，遞迴解）

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val              # 節點值
        self.left = left            # 左子樹
        self.right = right          # 右子樹

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:               # 若樹為空，直接回傳 None
            return None
        # 交換左右子樹
        root.left, root.right = root.right, root.left
        # 遞迴反轉左子樹
        self.invertTree(root.left)
        # 遞迴反轉右子樹
        self.invertTree(root.right)
        return root                # 回傳反轉後的根節點

# 範例測試
if __name__ == "__main__":
    def build_tree(nodes):
        # 由陣列建立二元樹（BFS）
        if not nodes:
            return None
        from collections import deque
        root = TreeNode(nodes[0])
        queue = deque([root])
        i = 1
        while queue and i < len(nodes):
            node = queue.popleft()
            if nodes[i] is not None:
                node.left = TreeNode(nodes[i])
                queue.append(node.left)
            i += 1
            if i < len(nodes) and nodes[i] is not None:
                node.right = TreeNode(nodes[i])
                queue.append(node.right)
            i += 1
        return root

    def tree_to_list(root):
        # 將二元樹轉為陣列（BFS）
        from collections import deque
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        # 移除尾端多餘的 None
        while result and result[-1] is None:
            result.pop()
        return result

    # 測試用例
    test_cases = [
        [4,2,7,1,3,6,9],
        [2,1,3],
        []
    ]
    for case in test_cases:
        root = build_tree(case)                 # 建立原始樹
        inv = Solution().invertTree(root)       # 反轉樹
        print(tree_to_list(inv))                # 輸出反轉後的陣列
```
```
