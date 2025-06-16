# 4. Median of Two Sorted Arrays

> 難度：Hard 🔴

> 題型：Array & Binary Search

## 題目描述
> 給定兩個已排序的陣列 nums1 和 nums2，分別長度為 m 和 n，請你找出這兩個已排序陣列的中位數。要求演算法的時間複雜度為 O(log (m+n))。

> Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

---

## 💡 解題思路
1. 由於兩個陣列皆已排序，可利用二分搜尋法（Binary Search）來達到 O(log(min(m, n))) 的時間複雜度。
2. 先確保 nums1 長度較短，對較短的陣列進行二分搜尋。
3. 設定分割點 i（nums1）與 j（nums2），使得左半部元素個數等於右半部。
4. 檢查分割點是否滿足條件：nums1[i-1] <= nums2[j] 且 nums2[j-1] <= nums1[i]。
5. 若不滿足，調整分割點繼續二分搜尋。
6. 找到正確分割後，根據總長度奇偶決定中位數。

> ⚠️ 注意：需處理邊界情況（如分割點在陣列開頭或結尾）。

---

## 📚 範例

| 輸入                | 輸出 |
|---------------------|------|
| nums1 = [1,3], nums2 = [2] | 2.0  |
| nums1 = [1,2], nums2 = [3,4] | 2.5  |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                                  |
|--------------|---------------------------------------|
| 使用資料結構 | 陣列、二分搜尋                        |
| 時間複雜度   | O(log(min(m, n)))                     |
| 空間複雜度   | O(1)                                  |
| 優點         | 時間複雜度低，適合大數據               |
| 缺點         | 邏輯較複雜，需處理多種邊界情況         |

---

## ⚡ 程式碼實作（Python）

```python
# 求兩個已排序陣列的中位數
from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    # 將 nums1, nums2 指派給 A, B
    A, B = nums1, nums2  # A, B 分別指向兩個輸入陣列
    # 計算兩陣列總長度
    total = len(A) + len(B)  # 兩陣列總長度
    # 計算左半部元素個數
    half = total // 2  # 左半部元素個數
    # 若 B 較短則交換，確保 A 為較短陣列
    if len(B) < len(A):  # 若 B 較短則交換
        A, B = B, A
    # 設定二分搜尋範圍
    l, r = 0, len(A) - 1  # l, r 為 A 的搜尋範圍
    while True:
        # A 的分割點
        i = (l + r) // 2  # A 的分割點
        # B 的分割點，確保左半部元素數量正確
        j = half - i - 2  # B 的分割點

        # 取得分割點左右的值，若越界則用無窮大/小處理
        Aleft = A[i] if i >= 0 else float('-inf')  # A 左半最大值
        Aright = A[i + 1] if (i + 1) < len(A) else float('inf')  # A 右半最小值
        Bleft = B[j] if j >= 0 else float('-inf')  # B 左半最大值
        Bright = B[j + 1] if (j + 1) < len(B) else float('inf')  # B 右半最小值
        
        # 檢查分割是否正確
        if Aleft <= Bright and Bleft <= Aright:  # 分割正確
            if total % 2:  # 若總長度為奇數
                return min(Aright, Bright)  # 回傳右半最小值
            # 否則回傳左半最大值與右半最小值平均
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:  # Aleft 太大，i 太大
            r = i - 1  # 往左縮小範圍
        else:  # Aleft 太小，i 太小
            l = i + 1  # 往右擴大範圍

if __name__ == "__main__":
    # 範例測試
    nums1 = [1, 3]  # 測試資料1
    nums2 = [2]     # 測試資料2
    print(findMedianSortedArrays(nums1, nums2))  # 預期輸出：2.0
    nums1 = [1, 2]  # 測試資料3
    nums2 = [3, 4]  # 測試資料4
    print(findMedianSortedArrays(nums1, nums2))  # 預期輸出：2.5
```
