# 105. Construct Binary Tree from Preorder and Inorder Traversal

> 難度：Medium 🟡

> 題型：Tree, DFS, Recursion

## 題目描述
> 給定兩個整數陣列 preorder 和 inorder，分別代表一棵二元樹的前序遍歷和中序遍歷，請根據這兩個遍歷結果重建並返回該二元樹的根節點。

> Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

---

## 💡 解題思路
1. 前序遍歷的第一個元素一定是樹的根節點。
2. 在中序遍歷中找到這個根節點，左邊是左子樹，右邊是右子樹。
3. 遞迴地對左子樹和右子樹重複上述步驟。
4. 利用哈希表加速中序索引查找。

> ⚠️ 注意：每次遞迴時要正確切分 preorder 和 inorder 的範圍。

---

## 📚 範例

| 輸入 | 輸出 |
|------|------|
| preorder = [3,9,20,15,7], inorder = [9,3,15,20,7] | [3,9,20,null,null,15,7] |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                                  |
|--------------|---------------------------------------|
| 使用資料結構 | 遞迴、哈希表、二元樹                  |
| 時間複雜度   | O(n)                                  |
| 空間複雜度   | O(n)（遞迴棧深與哈希表）              |
| 優點         | 邏輯清晰，利用哈希表加速查找           |
| 缺點         | 需額外空間存儲哈希表與遞迴棧           |

---

## 🧑‍💻 Python 範例程式碼

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # 節點值
        self.left = left  # 左子樹
        self.right = right  # 右子樹

# 主函式，重建二元樹
class Solution:
    def buildTree(self, preorder, inorder):
        # 建立中序值到索引的映射，加速查找
        inorder_index = {val: idx for idx, val in enumerate(inorder)}  # 哈希表

        def helper(pre_left, pre_right, in_left, in_right):
            # 若沒有元素，返回 None
            if pre_left > pre_right:
                return None
            # 前序的第一個元素是根節點
            root_val = preorder[pre_left]
            root = TreeNode(root_val)  # 建立根節點
            # 根節點在中序的位置
            in_root_idx = inorder_index[root_val]
            # 左子樹節點數量
            left_size = in_root_idx - in_left
            # 遞迴構建左子樹
            root.left = helper(pre_left+1, pre_left+left_size, in_left, in_root_idx-1)
            # 遞迴構建右子樹
            root.right = helper(pre_left+left_size+1, pre_right, in_root_idx+1, in_right)
            return root  # 返回根節點

        # 從整個區間開始遞迴
        return helper(0, len(preorder)-1, 0, len(inorder)-1)

# 範例測試
if __name__ == "__main__":
    preorder = [3,9,20,15,7]  # 前序遍歷
    inorder = [9,3,15,20,7]   # 中序遍歷
    sol = Solution()
    root = sol.buildTree(preorder, inorder)  # 構建樹

    # 輔助函式：層序遍歷輸出樹結構
    from collections import deque
    def print_tree(root):
        if not root:
            print([])
            return
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
        # 去除尾部多餘的 None
        while result and result[-1] is None:
            result.pop()
        print(result)
    print_tree(root)  # 輸出: [3, 9, 20, None, None, 15, 7]
```
