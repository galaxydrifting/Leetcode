# 239. Sliding Window Maximum

> 難度：Hard 🔴

## 題目描述
> 給定一個整數陣列 nums，以及一個大小為 k 的滑動視窗，視窗會從陣列最左側移動到最右側。每次移動時，你只能看到視窗內的 k 個數字。請回傳每次視窗移動時的最大值。

> You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

---

> 題型：Sliding Window & Monotonic Queue

---

## 💡 解題思路
1. 使用雙端佇列（deque）來維護一個單調遞減的索引隊列。
2. 每次新元素進入時，將隊尾小於新元素的索引全部移除，確保隊列單調遞減。
3. 若隊首索引已經滑出視窗範圍，則將其移除。
4. 當視窗長度達到 k 時，將隊首對應的元素（即當前最大值）加入結果。

> ⚠️ 雙端佇列可在 O(1) 時間內取得最大值，確保整體時間複雜度為 O(n)。

---

## 📚 範例

| 輸入                | 輸出      |
|---------------------|-----------|
| nums = [1,3,-1,-3,5,3,6,7], k = 3 | [3,3,5,5,6,7] |
| nums = [1], k = 1   | [1]       |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                        |
|--------------|-----------------------------|
| 使用資料結構 | 雙端佇列（deque）           |
| 時間複雜度   | O(n)                        |
| 空間複雜度   | O(k)                        |
| 優點         | 可高效取得視窗最大值         |
| 缺點         | 需額外空間維護佇列           |

---

## ⚡ 程式碼實作（Python）

```python
from typing import List
import collections  # 匯入 collections 模組以使用 deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []  # 儲存每個視窗的最大值
        q = collections.deque()  # 用來存放索引，維持單調遞減
        l = r = 0  # l: 左指標, r: 右指標

        while r < len(nums):
            # 移除隊尾小於當前元素的索引，確保隊列單調遞減
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # 移除已滑出視窗的隊首索引
            if l > q[0]:
                q.popleft()

            # 當視窗長度達到 k 時，將最大值加入結果
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1  # 左指標右移，縮小視窗
            r += 1  # 右指標右移，擴大視窗

        return output

if __name__ == "__main__":
    # 範例測試
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(Solution().maxSlidingWindow(nums, k))  # 輸出: [3,3,5,5,6,7]
    nums2 = [1]
    k2 = 1
    print(Solution().maxSlidingWindow(nums2, k2))  # 輸出: [1]
```
