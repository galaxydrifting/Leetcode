# 238. Product of Array Except Self

> 難度：Medium 🟡

> 題型：Array & Prefix Product

## 題目描述
> 給定一個整數陣列 nums，請回傳一個陣列 answer，其中 answer[i] 等於 nums 陣列中除了 nums[i] 以外所有元素的乘積。
> 
> 陣列的任何前綴或後綴的乘積都保證能在 32 位元整數範圍內。
> 
> 你必須設計一個時間複雜度為 O(n) 且不能使用除法運算的演算法。
>
> Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
>
> The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
>
> You must write an algorithm that runs in O(n) time and without using the division operation.

---

## 💡 解題思路
1. 先建立一個與 nums 等長的陣列 answer，初始值皆為 1。
2. 從左到右遍歷 nums，計算每個位置左側所有元素的乘積，存入 answer。
3. 再從右到左遍歷 nums，計算每個位置右側所有元素的乘積，並與 answer 中對應位置相乘。
4. 最終 answer 即為所求。

> ⚠️ 不能用除法，需分別計算左側與右側乘積。

---

## 📚 範例

| 輸入           | 輸出        |
|----------------|-------------|
| [1,2,3,4]      | [24,12,8,6] |
| [-1,1,0,-3,3]  | [0,0,9,0,0] |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                        |
|--------------|-----------------------------|
| 使用資料結構 | 陣列                        |
| 時間複雜度   | O(n)                        |
| 空間複雜度   | O(1)（不含輸出陣列）        |
| 優點         | 無需除法，單次遍歷即可完成  |
| 缺點         | 需額外空間存儲乘積資訊      |

---

## ⚡ 程式碼實作（Python）

```python
from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    answer = [1] * n
    left = 1
    for i in range(n):
        answer[i] = left
        left *= nums[i]
    right = 1
    for i in range(n-1, -1, -1):
        answer[i] *= right
        right *= nums[i]
    return answer
```
