# 153. Find Minimum in Rotated Sorted Array

> 難度：Medium 🟡

> 題型：Binary Search（二分搜尋）、Array & Hashing

## 題目描述
> 給定一個已排序（升序）但經過旋轉的陣列（元素唯一），請找出其中的最小值。必須以 O(log n) 時間複雜度完成。

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

---

## 💡 解題思路
1. 使用二分搜尋法（Binary Search）來縮小搜尋範圍。
2. 設定左右指標 left、right，初始分別指向陣列首尾。
3. 每次取中間值 mid，判斷 nums[mid] 是否小於 nums[right]：
   - 若是，代表最小值在左半邊（包含 mid），將 right 移到 mid。
   - 否則，最小值在右半邊（不包含 mid），將 left 移到 mid + 1。
4. 當 left == right 時，即為最小值所在位置。

> ⚠️ 注意：陣列中所有元素皆唯一，且必有解。

---

## 📚 範例

| 輸入                | 輸出 |
|---------------------|------|
| [3,4,5,1,2]         | 1    |
| [4,5,6,7,0,1,2]     | 0    |
| [11,13,15,17]       | 11   |
| [1]                 | 1    |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                         |
|--------------|------------------------------|
| 使用資料結構 | 陣列（Array）                |
| 時間複雜度   | O(log n)（二分搜尋）         |
| 空間複雜度   | O(1)（只用常數額外空間）     |
| 優點         | 高效搜尋，適用大數據         |
| 缺點         | 僅適用於已排序且無重複元素   |

---

## ⚡ 程式碼實作（Python）

```python
# 使用二分搜尋法尋找旋轉排序陣列中的最小值
class Solution:
    def findMin(self, nums):
        left = 0  # 左指標，指向陣列開頭
        right = len(nums) - 1  # 右指標，指向陣列結尾
        while left < right:  # 當左右指標未重疊時持續搜尋
            mid = (left + right) // 2  # 取中間索引
            if nums[mid] < nums[right]:  # 若中間值小於右端值
                right = mid  # 最小值在左半邊（包含 mid）
            else:  # 否則最小值在右半邊
                left = mid + 1  # 移動左指標到 mid 右側
        return nums[left]  # 返回最小值
```
