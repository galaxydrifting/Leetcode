# 0042. Trapping Rain Water

> 難度：Hard 🔴

> 題型：Array & Two Pointers

## 題目描述
> 給定 n 個非負整數，代表每個寬度為 1 的柱子的高度，請計算下雨後這些柱子能接住多少雨水。

> Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

---

## 💡 解題思路
1. 使用雙指針（left, right）分別從左右兩端往中間移動。
2. 維護左右兩側的最大高度（left_max, right_max）。
3. 每次比較 left_max 與 right_max，較小的一側決定當前能接的水量。
4. 若 left_max < right_max，則左側可接水量為 left_max - height[left]，然後左指針右移。
5. 反之則右側可接水量為 right_max - height[right]，然後右指針左移。
6. 重複直到 left >= right。

> ⚠️ 注意：每個位置能接的水量取決於其左右最大高度的較小值減去當前高度。

---

## 📚 範例

![rainwatertrap](rainwatertrap.png)

| 輸入                | 輸出 |
|---------------------|------|
| [0,1,0,2,1,0,1,3,2,1,2,1] | 6    |
| [4,2,0,3,2,5]       | 9    |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                                  |
|--------------|---------------------------------------|
| 使用資料結構 | 陣列、雙指針                          |
| 時間複雜度   | O(n)                                 |
| 空間複雜度   | O(1)                                 |
| 優點         | 單次遍歷即可完成，效率高               |
| 缺點         | 需理解雙指針與左右最大高度的邏輯       |

---

## ⚡ 程式碼實作（Python）

```python
class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += max(0, left_max - height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += max(0, right_max - height[right])
        return water
```
