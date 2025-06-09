# 167. Two Sum II - Input Array Is Sorted

> 難度：Medium 🟡  
> 題型：Array & Two Pointers

## 題目描述

> 給定一個已按照非遞減順序排序的 1-indexed 整數陣列 numbers，請找出兩個數字，使它們的和等於指定的 target。  
> 回傳這兩個數字的索引（index1, index2），索引需加一（即 1-based），且 1 <= index1 < index2 <= numbers.length。  
> 每個輸入保證只有一組解答，且不能重複使用同一個元素。

> Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.  
> Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.  
> You may not use the same element twice. The tests are generated such that there is exactly one solution.

---

## 💡 解題思路

1. 使用「雙指標」法：一個指標 left 從陣列開頭，另一個 right 從陣列結尾。
2. 計算 numbers[left] + numbers[right]：
   - 若等於 target，回傳 [left+1, right+1]。
   - 若小於 target，left 向右移動（left += 1）。
   - 若大於 target，right 向左移動（right -= 1）。
3. 因為陣列已排序，這種方式能保證找到唯一解且只需 O(1) 額外空間。

> ⚠️ 注意：題目要求只能用常數額外空間，不能用 hash table。

---

## 📚 範例

| 輸入                | 輸出    |
|---------------------|---------|
| numbers = [2,7,11,15], target = 9  | [1,2]  |
| numbers = [2,3,4], target = 6      | [1,3]  |
| numbers = [-1,0], target = -1      | [1,2]  |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                                  |
|--------------|---------------------------------------|
| 使用資料結構 | 雙指標（Two Pointers）                |
| 時間複雜度   | O(n)                                  |
| 空間複雜度   | O(1)                                  |
| 優點         | 不需額外空間，利用排序特性高效搜尋    |
| 缺點         | 僅適用於已排序陣列                    |

---

## ⚡ 程式碼實作（Python）

```python
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left + 1, right + 1]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
```
