# 11. Container With Most Water

> 難度：Medium 🟡

> 題型：Array & Two Pointers

## 題目描述
> 給定一個長度為 n 的整數陣列 height，陣列中的每個元素代表一條直線的高度。每條直線的兩端點分別為 (i, 0) 和 (i, height[i])。
> 
> 請找出其中兩條直線，與 x 軸共同構成的容器能容納的最大水量。
> 
> 注意：容器不能傾斜。

> Given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
>
> Find two lines that together with the x-axis form a container, such that the container contains the most water.
>
> Notice that you may not slant the container.

---

## 💡 解題思路
1. 使用雙指針法，分別指向陣列的開頭與結尾。
2. 計算當前兩指針所圍成的容器面積，並更新最大值。
3. 移動高度較小的指針，因為只有這樣才有機會找到更大的面積。
4. 重複步驟 2-3，直到兩指針相遇。

> ⚠️ 只有移動較短邊才有機會增加面積，因為寬度會變小。

---

## 📚 範例

| 輸入                | 輸出 |
|---------------------|------|
| height = [1,8,6,2,5,4,8,3,7] | 49   |
| height = [1,1]      | 1    |

> ![Container Visual](./question_11.jpg)
> 
> [圖片來源：LeetCode](https://leetcode.com/problems/container-with-most-water/description/)

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                |
|--------------|---------------------|
| 使用資料結構 | 陣列、雙指針        |
| 時間複雜度   | O(n)                |
| 空間複雜度   | O(1)                |
| 優點         | 一次遍歷即可完成，效率高 |
| 缺點         | 需理解雙指針移動邏輯   |

---

## ⚡ 程式碼實作（Python）

```python
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            max_water = max(max_water, h * w)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water
```
