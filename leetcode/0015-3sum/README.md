# 15. 3Sum

> 難度：Medium 🟡

> 題型：Array & Two Pointers

## 題目描述
> 給定一個整數陣列 nums，請你找出所有不重複的三元組 [nums[i], nums[j], nums[k]]，使得 i ≠ j、i ≠ k、j ≠ k，且 nums[i] + nums[j] + nums[k] == 0。

> Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

> 注意：解集合中不可包含重複的三元組。

---

## 💡 解題思路
1. 先將陣列排序，方便去除重複解。
2. 固定一個數字 nums[i]，用雙指針在剩下的區間內尋找另外兩個數字，使三數和為 0。
3. 若總和大於 0，右指針左移；若總和小於 0，左指針右移。
4. 跳過重複的數字以避免重複解。

> ⚠️ 注意：排序後才能有效去除重複三元組。

---

## 📚 範例

| 輸入                | 輸出                                 |
|---------------------|--------------------------------------|
| nums = [-1,0,1,2,-1,-4] | [[-1,-1,2],[-1,0,1]]                |
| nums = [0,1,1]      | []                                   |
| nums = [0,0,0]      | [[0,0,0]]                            |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                        |
|--------------|-----------------------------|
| 使用資料結構 | 陣列、雙指針                |
| 時間複雜度   | O(n^2)                      |
| 空間複雜度   | O(1)（不含輸出結果空間）    |
| 優點         | 不需額外空間，效率高         |
| 缺點         | 需先排序，對大數據排序耗時   |

---

## ⚡ 程式碼實作（Python）

```python
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        result = []

        for idx, n in enumerate(nums):
            if idx > 0 and n == nums[idx - 1]:
                continue

            l, r = idx + 1, length - 1

            while l < r:
                three_sum = n + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    result.append([n, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return result
```
