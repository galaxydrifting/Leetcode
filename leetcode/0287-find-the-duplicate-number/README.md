# 287. Find the Duplicate Number

> 難度：Medium 🟡

> 題型：Array & Two Pointers

## 題目描述
給定一個包含 n + 1 個整數的陣列 `nums`，其中每個整數都在區間 [1, n] 之間（包含 1 和 n）。
陣列中只有一個數字重複出現，請找出這個重複的數字。

> Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
> There is only one repeated number in nums, return this repeated number.

**限制條件：**
- 你不能修改陣列（假設為只讀）。
- 只能使用常數級額外空間。
- 時間複雜度需優於 O(n²)。

---

## 💡 解題思路
1. 由於數字範圍為 [1, n]，且陣列長度為 n+1，必有重複數字（鴿巢原理）。
2. 不能修改陣列且只能用常數空間，常見解法有：
   - 快慢指針（Floyd's Tortoise and Hare）將陣列視為鏈結串列找循環入口。
3. 具體步驟：
   1. 設定快慢指針，初始都指向陣列第一個元素。
   2. 快指針每次走兩步，慢指針每次走一步，直到相遇。
   3. 其中一指針回到起點，兩指針每次都走一步，再次相遇時即為重複數字。

> ⚠️ 不能排序或改動原陣列，也不能用 set/dict 等額外空間。

---

## 📚 範例

| 輸入           | 輸出 |
|----------------|------|
| [1,3,4,2,2]    | 2    |
| [3,1,3,4,2]    | 3    |
| [1,1]          | 1    |
| [1,1,2]        | 1    |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                                   |
|--------------|----------------------------------------|
| 使用資料結構 | 快慢指針（Floyd's Cycle Detection）     |
| 時間複雜度   | O(n)                                   |
| 空間複雜度   | O(1)                                   |
| 優點         | 不需修改原陣列，空間複雜度低            |
| 缺點         | 需理解快慢指針找循環入口的原理          |

---

## 🧑‍💻 程式碼（Python，含註解）

```python
# 287. Find the Duplicate Number
from typing import List

def findDuplicate(nums: List[int]) -> int:
    # 初始化快慢指針，皆指向陣列第一個元素
    slow = nums[0]  # 慢指針
    fast = nums[0]  # 快指針
    # 第一階段：快慢指針相遇
    while True:
        slow = nums[slow]        # 慢指針走一步
        fast = nums[nums[fast]] # 快指針走兩步
        if slow == fast:        # 相遇則跳出
            break
    # 第二階段：尋找循環入口
    slow = nums[0]              # 慢指針回到起點
    while slow != fast:
        slow = nums[slow]       # 慢指針走一步
        fast = nums[fast]       # 快指針走一步
    return slow                 # 相遇點即為重複數字
```

---
