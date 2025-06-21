# 124. Binary Tree Maximum Path Sum

> 難度：Hard 🔴

> 題型：Tree, DFS, Dynamic Programming

## 題目描述
> 給定一個二元樹，請你找出路徑和最大的路徑。路徑可以從樹中的任何節點出發和結束，但必須沿著父子連結向下或向上連續移動，且每個節點只能出現一次。

> Given the root of a binary tree, return the maximum path sum of any non-empty path. A path is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. The path does not need to pass through the root.

---

## 💡 解題思路
1. 使用 DFS 遍歷每個節點，計算經過該節點的最大路徑和。
2. 對於每個節點，計算左子樹和右子樹的最大貢獻值（如果小於 0 則視為 0）。
3. 當前節點的最大路徑和為：節點值 + 左貢獻 + 右貢獻。
4. 全域變數記錄全樹最大路徑和。
5. 回傳給父節點的值只能選擇一邊（左或右）加上自己。

> ⚠️ 注意：路徑可以不經過 root，也可以只包含單一節點。

---

## 📚 範例

| 輸入 | 輸出 |
|------|------|
| root = [1,2,3] | 6 |
| root = [-10,9,20,null,null,15,7] | 42 |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                |
|--------------|---------------------|
| 使用資料結構 | 二元樹、遞迴         |
| 時間複雜度   | O(N)                |
| 空間複雜度   | O(H)（H 為樹高）     |
| 優點         | 一次 DFS 即可求解    |
| 缺點         | 需理解遞迴回傳意義   |

---

## Python 程式碼

```python
# ...請見 solution.py ...
```
