# 74. Search a 2D Matrix

> 難度：Medium 🟡

> 題型：Binary Search, Matrix

## 題目描述
> 給定一個 m x n 的整數矩陣 matrix，具有以下兩個特性：
> 1. 每一列皆以非遞減順序排序。
> 2. 每一列的第一個整數大於前一列的最後一個整數。
> 請判斷給定的整數 target 是否存在於 matrix 中。

> Given an m x n integer matrix matrix with the following two properties:
> 1. Each row is sorted in non-decreasing order.
> 2. The first integer of each row is greater than the last integer of the previous row.
> Given an integer target, return true if target is in matrix or false otherwise.

---

## 💡 解題思路
1. 將整個 2D 矩陣視為一個一維遞增陣列。
2. 使用二分搜尋法（Binary Search）於此一維陣列上搜尋 target。
3. 透過 index // n 及 index % n 轉換一維索引至二維座標。
4. 若找到 target 則回傳 True，否則回傳 False。

> ⚠️ 注意：必須將二維座標與一維索引正確轉換，避免越界。

---

## 📚 範例

![matrix example](mat.jpg)

| 輸入 | 輸出 |
|------|------|
| matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3 | True |
| matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13 | False |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                        |
|--------------|-----------------------------|
| 使用資料結構 | 陣列（Array）               |
| 時間複雜度   | O(log(m * n))               |
| 空間複雜度   | O(1)                        |
| 優點         | 時間效率高，無需額外空間    |
| 缺點         | 需理解二維與一維索引轉換    |

---

## ⚡ 程式碼實作（Python）

```python
# 二分搜尋法於 2D 矩陣
class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)  # 取得矩陣的列數
        n = len(matrix[0]) if m > 0 else 0  # 取得矩陣的行數
        left = 0  # 一維陣列的起始索引
        right = m * n - 1  # 一維陣列的結束索引
        while left <= right:  # 當搜尋區間有效時
            mid = (left + right) // 2  # 取中間索引
            row, col = divmod(mid, n)  # 同時計算列與行，使用 divmod 使程式更簡潔
            val = matrix[row][col]  # 取得對應元素
            if val == target:  # 若找到目標
                return True  # 回傳 True
            elif val < target:  # 若中間值小於目標
                left = mid + 1  # 移動左界
            else:  # 若中間值大於目標
                right = mid - 1  # 移動右界
        return False  # 未找到目標，回傳 False
```
