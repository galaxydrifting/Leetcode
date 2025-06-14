# 33. Search in Rotated Sorted Array

> 難度：Medium 🟡

> 題型：Array & Binary Search

## 題目描述
> 給定一個已經按照升序排列且元素不重複的整數陣列 `nums`，該陣列可能在某個未知的樞紐點進行了旋轉（1 <= k < nums.length），例如 `[0,1,2,4,5,6,7]` 可能在索引 3 處旋轉成 `[4,5,6,7,0,1,2]`。
> 
> 請實作一個函式，給定旋轉後的陣列 `nums` 和一個目標值 `target`，如果 `target` 存在於陣列中，回傳其索引，否則回傳 -1。
> 
> The array is sorted in ascending order and rotated at an unknown pivot. Implement an algorithm with O(log n) time complexity to find the target's index or return -1 if not found.

---

## 💡 解題思路
1. 使用二分搜尋法（Binary Search），每次判斷哪一半是有序的。
2. 根據有序區間判斷 target 是否落在該區間，決定搜尋左半或右半。
3. 持續縮小搜尋範圍，直到找到目標或區間為空。

> ⚠️ 注意：必須保證時間複雜度為 O(log n)，不能用線性搜尋。

---

## 📚 範例

| 輸入                | 輸出 |
|---------------------|------|
| nums = [4,5,6,7,0,1,2], target = 0 | 4    |
| nums = [4,5,6,7,0,1,2], target = 3 | -1   |
| nums = [1], target = 0             | -1   |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                |
|--------------|---------------------|
| 使用資料結構 | 陣列                |
| 時間複雜度   | O(log n)            |
| 空間複雜度   | O(1)                |
| 優點         | 搜尋速度快，適合大數據集 |
| 缺點         | 需理解旋轉後的二分搜尋邏輯 |

---

## ⚡ 程式碼實作（Python）

```python
# 搜尋旋轉排序陣列
from typing import List

def search(nums: List[int], target: int) -> int:
    left = 0  # 左指標
    right = len(nums) - 1  # 右指標
    while left <= right:  # 當左指標不超過右指標時
        mid = (left + right) // 2  # 取中間索引
        if nums[mid] == target:  # 若找到目標
            return mid  # 回傳索引
        # 判斷哪一半是有序的
        if nums[left] <= nums[mid]:  # 左半邊有序
            if nums[left] <= target < nums[mid]:  # 目標在左半邊
                right = mid - 1  # 縮小右邊界
            else:
                left = mid + 1  # 否則搜尋右半邊
        else:  # 右半邊有序
            if nums[mid] < target <= nums[right]:  # 目標在右半邊
                left = mid + 1  # 縮小左邊界
            else:
                right = mid - 1  # 否則搜尋左半邊
    return -1  # 未找到目標

if __name__ == "__main__":
    # 範例測試
    nums1 = [4,5,6,7,0,1,2]
    print(search(nums1, 0))  # 輸出: 4
    print(search(nums1, 3))  # 輸出: -1
    nums2 = [1]
    print(search(nums2, 0))  # 輸出: -1
```
```
