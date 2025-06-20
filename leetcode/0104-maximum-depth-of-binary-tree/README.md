# 104. Maximum Depth of Binary Tree

> 難度：Easy 🟢

> 題型：Tree, DFS, BFS

## 題目描述
給定一個二元樹的根節點，請你返回其最大深度。

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

給定一棵二元樹，最大深度是從根節點到最遠葉子節點的最長路徑上的節點數。

---

## 💡 解題思路
1. 若節點為空，則深度為 0。
2. 遞迴計算左子樹與右子樹的最大深度。
3. 取左右子樹最大深度後加 1（包含當前節點）。

---

## 📚 範例

| 輸入 | 輸出 |
|------|------|
| root = [3,9,20,null,null,15,7] | 3 |
| root = [1,null,2] | 2 |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                |
|--------------|---------------------|
| 使用資料結構 | 二元樹、遞迴         |
| 時間複雜度   | O(n)                |
| 空間複雜度   | O(h)（h 為樹高）     |
| 優點         | 實作簡單、易於理解   |
| 缺點         | 遞迴深度過深時可能導致堆疊溢位 |

---

## 🧑‍💻 程式碼（Python，含註解）

（請參考 solution.py 檔案，內含三種解法：遞迴 DFS、BFS、迭代 DFS，並有完整註解與測試範例）
