# 543. Diameter of Binary Tree

> 難度：Easy 🟢

> 題型：Tree, DFS, Binary Tree

## 題目描述

> 給定一個二元樹的根節點 `root`，請返回該樹的直徑長度。
> 
> 二元樹的直徑是指樹中任意兩個節點之間最長路徑的邊數。這條路徑可能會經過根節點，也可能不會。

---

## 💡 解題思路
1. 使用深度優先搜尋（DFS）遍歷整棵樹。
2. 對於每個節點，計算其左子樹和右子樹的最大深度。
3. 以當前節點為「中繼點」時，左深度 + 右深度 即為經過該節點的最大直徑。
4. 遍歷過程中持續更新全域最大直徑。
5. 最終回傳最大直徑。

> ⚠️ 注意：直徑是「邊」的數量，不是「節點」的數量。

---

## 📚 範例

| 輸入 | 輸出 |
|------|------|
| root = [1,2,3,4,5] | 3 |
| root = [1,2] | 1 |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                |
|--------------|---------------------|
| 使用資料結構 | 二元樹、遞迴         |
| 時間複雜度   | O(n)                |
| 空間複雜度   | O(n)（遞迴棧最深 n） |
| 優點         | 一次 DFS 即可求解    |
| 缺點         | 遞迴需額外棧空間     |

---

## 🧑‍💻 程式碼（Python，含註解）

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # 節點值
        self.left = left  # 左子節點
        self.right = right  # 右子節點

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_diameter = 0  # 初始化最大直徑

        def dfs(node):
            if not node:
                return 0  # 空節點深度為 0
            left_depth = dfs(node.left)  # 遞迴獲取左子樹深度
            right_depth = dfs(node.right)  # 遞迴獲取右子樹深度
            # 更新最大直徑（左深度 + 右深度）
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)
            return max(left_depth, right_depth) + 1  # 回傳該節點的最大深度

        dfs(root)  # 從根節點開始 DFS
        return self.max_diameter  # 回傳最大直徑

# 範例測試
if __name__ == "__main__":
    # 建立範例二元樹 root = [1,2,3,4,5]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    sol = Solution()
    print(sol.diameterOfBinaryTree(root))  # 輸出 3
```
