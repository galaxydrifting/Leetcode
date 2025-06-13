# 875. Koko Eating Bananas

> 難度：Medium 🟡

> 題型：Binary Search

## 題目描述
> Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
>
> Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
>
> Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
>
> Return the minimum integer k such that she can eat all the bananas within h hours.

---

> 難度：中等 🟡

> 題型：二分搜尋

> Koko 喜歡吃香蕉。有 n 堆香蕉，第 i 堆有 piles[i] 根香蕉。守衛離開後會在 h 小時後回來。
>
> Koko 可以決定每小時吃香蕉的速度 k。每小時，她會選擇一堆香蕉，吃掉 k 根。如果該堆剩下的香蕉少於 k 根，她就全部吃完，該小時不再吃其他香蕉。
>
> Koko 想慢慢吃，但又必須在守衛回來前吃完所有香蕉。
>
> 請回傳能在 h 小時內吃完所有香蕉的最小整數 k。

---

## 💡 解題思路
1. 觀察到吃香蕉速度 k 越大，所需時間越短，適合用二分搜尋法找最小可行的 k。
2. 設定搜尋範圍為 [1, max(piles)]。
3. 每次猜一個速度 mid，計算以該速度吃完所有香蕉所需的總小時數。
4. 若總小時數小於等於 h，代表速度可以更慢，縮小右界；否則需加快速度，調整左界。
5. 最終找到的左界即為答案。

> ⚠️ 注意：每小時只能選一堆香蕉吃，不能同時吃多堆。

---

## 📚 範例

| 輸入 | 輸出 |
|------|------|
| piles = [3,6,7,11], h = 8 | 4 |
| piles = [30,11,23,4,20], h = 5 | 30 |
| piles = [30,11,23,4,20], h = 6 | 23 |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                         |
|--------------|------------------------------|
| 使用資料結構 | 陣列                         |
| 時間複雜度   | O(n * log(max(piles)))       |
| 空間複雜度   | O(1)                         |
| 優點         | 高效搜尋最小可行解           |
| 缺點         | 需理解二分搜尋的應用場景     |

---

## ⚡ 程式碼實作（Python）

```python
# 二分搜尋法找最小吃香蕉速度
from typing import List
import math  # 匯入 math 模組以使用 ceil 函式

def minEatingSpeed(piles: List[int], h: int) -> int:
    left = 1  # 最小速度設為1
    right = max(piles)  # 最大速度設為最大堆香蕉數
    while left < right:  # 當左界小於右界時持續搜尋
        mid = (left + right) // 2  # 取中間速度
        hours = 0  # 初始化總小時數
        for pile in piles:  # 遍歷每一堆香蕉
            hours += math.ceil(pile / mid)  # 使用 math.ceil 向上取整計算吃完該堆所需小時數
        if hours <= h:  # 如果總小時數小於等於h
            right = mid  # 嘗試更慢的速度
        else:
            left = mid + 1  # 需要更快的速度
    return left  # 返回最小可行速度
```
