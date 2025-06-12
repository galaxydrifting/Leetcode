# 84. Largest Rectangle in Histogram

> 難度：Hard 🔴

> 題型：Stack & Array

## 題目描述
給定一個整數陣列 `heights`，每個元素代表直方圖中每個柱子的高度，且每個柱子的寬度為 1。請回傳直方圖中，能夠構成的最大矩形面積。

> Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

---

## 💡 解題思路
1. 使用單調遞增堆疊（stack）來追蹤柱子的索引。
2. 當遇到比堆疊頂端柱子矮的柱子時，彈出堆疊並計算以該柱子為高的最大矩形面積。
3. 為了確保所有柱子都能被處理，最後在 heights 陣列後面補上一個 0。
4. 每次計算面積時，寬度為當前索引與堆疊新頂端索引之間的距離。

---

## 📚 範例

![](./histogram.jpg)

| 輸入             | 輸出 |
|------------------|------|
| [2,1,5,6,2,3]    | 10   |
| [2,4]            | 4    |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                        |
|--------------|-----------------------------|
| 使用資料結構 | Stack（堆疊）               |
| 時間複雜度   | O(n)                        |
| 空間複雜度   | O(n)                        |
| 優點         | 單次遍歷即可完成，效率高     |
| 缺點         | 需額外 stack 空間            |

---

## ⚡ 程式碼實作（Python）

```python
from typing import List

def largestRectangleArea(heights: List[int]) -> int:
    stack = []  # 儲存索引
    max_area = 0
    heights.append(0)  # 在最後加一個 0，確保所有柱子都會被處理
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    heights.pop()  # 還原 heights
    return max_area
```
