# 128. Longest Consecutive Sequence

> 難度：Medium 🟡

> 題型：Array & Hashing

## 題目描述
> 給定一個未排序的整數陣列 nums，請找出最長的連續元素序列（元素值需連續且順序不限），並回傳其長度。
> 
> 你必須設計並實作一個時間複雜度為 O(n) 的演算法。

---

> Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
>
> You must write an algorithm that runs in O(n) time.

---

## 💡 解題思路
1. 將所有數字放入 HashSet 以便 O(1) 查找。
2. 遍歷每個數字，僅當該數字為序列起點（即 num-1 不在 set 中）時開始計算連續長度。
3. 依序檢查 num+1, num+2... 是否存在於 set 中，並累加長度。
4. 更新最長連續序列長度。

> ⚠️ 只從序列起點開始計算可避免重複計算，確保 O(n) 時間複雜度。

---

## 📚 範例

| 輸入                | 輸出 |
|---------------------|------|
| [100,4,200,1,3,2]   | 4    |
| [0,3,7,2,5,8,4,6,0,1] | 9    |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                                  |
|--------------|---------------------------------------|
| 使用資料結構 | HashSet（集合）                       |
| 時間複雜度   | O(n)                                  |
| 空間複雜度   | O(n)                                  |
| 優點         | 查找與插入皆為 O(1)，效率高            |
| 缺點         | 額外使用 O(n) 空間                    |

---

## ⚡ 程式碼實作（Python）

```python
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in num_set:
            length = 0

            if (n - 1) not in num_set:
                while (n + length) in num_set:
                    length += 1
                
                longest = max(longest, length)

        return longest
```
