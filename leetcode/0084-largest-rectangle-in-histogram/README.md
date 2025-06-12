# 84. Largest Rectangle in Histogram

> 難度：Hard 🔴

> 題型：Stack & Monotonic Stack

## 題目描述
> 給定一個整數陣列 heights，代表直方圖中每個柱子的高度，每個柱子的寬度為 1，請回傳直方圖中能夠形成的最大矩形面積。

> Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

---

## 💡 解題思路
1. 使用單調遞增堆疊（Monotonic Stack）來追蹤柱子的索引。
2. 當遇到比堆疊頂端柱子矮的柱子時，開始計算以堆疊頂端柱子為高的最大矩形面積。
3. 持續彈出堆疊並計算面積，直到堆疊為空或遇到更矮的柱子。
4. 最後將剩餘柱子也一併計算。

> ⚠️ 記得在 heights 後面補上一個 0，確保所有柱子都能被正確計算。

---

## 📚 範例

| 輸入           | 輸出 |
|----------------|------|
| [2,1,5,6,2,3]  | 10   |
| [2,4]          | 4    |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                        |
|--------------|-----------------------------|
| 使用資料結構 | 單調堆疊（Monotonic Stack） |
| 時間複雜度   | O(n)                        |
| 空間複雜度   | O(n)                        |
| 優點         | 高效處理所有柱子的情境      |
| 缺點         | 需額外堆疊空間              |

---

## ⚡ 程式碼實作（Python）

```python
# 使用單調堆疊求解最大矩形面積
class Solution:
    def largestRectangleArea(self, heights):
        heights.append(0)  # 在 heights 後補 0，確保所有柱子都能被計算
        stack = []  # 初始化堆疊，存放柱子的索引
        max_area = 0  # 最大面積初始為 0
        for i, h in enumerate(heights):  # 遍歷每個柱子
            # 當堆疊不為空且當前高度小於堆疊頂端高度時
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]  # 取出堆疊頂端的高度
                # 如果堆疊為空，寬度就是 i，否則是 i - stack[-1] - 1
                width = i if not stack else i - stack[-1] - 1
                area = height * width  # 計算面積
                max_area = max(max_area, area)  # 更新最大面積
            stack.append(i)  # 將當前索引加入堆疊
        return max_area  # 回傳最大面積
```
