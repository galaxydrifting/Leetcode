# 704. Binary Search

> 難度：Easy 🟢

> 題型：Array & Binary Search

## 題目描述
> 給定一個已排序（遞增）的整數陣列 nums，以及一個整數 target，請實作一個函式搜尋 target 是否存在於 nums 中。
> 若存在，回傳其索引；否則回傳 -1。

> Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

---

## 💡 解題思路
1. 使用二分搜尋法（Binary Search），每次將搜尋範圍對半縮小。
2. 設定左右指標 left、right，初始分別為 0 與陣列長度減一。
3. 進行迴圈，當 left <= right 時：
   - 取中間索引 mid = (left + right) // 2。
   - 若 nums[mid] == target，回傳 mid。
   - 若 nums[mid] < target，將 left 設為 mid + 1。
   - 若 nums[mid] > target，將 right 設為 mid - 1。
4. 若迴圈結束仍未找到，回傳 -1。

> ⚠️ 注意：必須保證時間複雜度為 O(log n)。

---

## 📚 範例

| 輸入                | 輸出 |
|---------------------|------|
| nums = [-1,0,3,5,9,12], target = 9  | 4    |
| nums = [-1,0,3,5,9,12], target = 2  | -1   |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                |
|--------------|---------------------|
| 使用資料結構 | 陣列                |
| 時間複雜度   | O(log n)            |
| 空間複雜度   | O(1)                |
| 優點         | 查找速度快，效率高  |
| 缺點         | 僅適用於已排序陣列  |

---

## ⚡ 程式碼實作（Python）

```python
# 二分搜尋法實作
# nums: 已排序的整數陣列
# target: 要搜尋的目標值
# 回傳 target 的索引，若不存在則回傳 -1

def search(nums, target):
    left = 0  # 左指標，起始為 0
    right = len(nums) - 1  # 右指標，起始為陣列最後一個索引
    while left <= right:  # 當左指標不超過右指標時持續搜尋
        mid = (left + right) // 2  # 取中間索引
        if nums[mid] == target:  # 若中間值等於目標值
            return mid  # 回傳索引
        elif nums[mid] < target:  # 若中間值小於目標值
            left = mid + 1  # 移動左指標到 mid 右邊
        else:  # 若中間值大於目標值
            right = mid - 1  # 移動右指標到 mid 左邊
    return -1  # 若未找到目標值，回傳 -1
```

## ⚠️ Java 實作時的 Overflow 注意事項

在 Java 中，若直接使用 `mid = (left + right) / 2`，當 `left` 和 `right` 都很大時，`left + right` 可能會超過 int 的最大值，導致 overflow。

**正確寫法：**
```java
int mid = left + (right - left) / 2;
```
這樣可以避免 overflow，因為 `right - left` 不會超過 int 範圍。

**錯誤寫法（可能 overflow）：**
```java
int mid = (left + right) / 2;
```

---

### C# 也有 Overflow 的可能嗎？

是的，C# 的 `int` 也是 32 位元，若直接寫 `int mid = (left + right) / 2;`，當 `left` 和 `right` 都很大時，`left + right` 也可能溢位。

**正確寫法：**
```csharp
int mid = left + (right - left) / 2;
```
這樣同樣可以避免 overflow。

---

### 為什麼 `l + (r - l) / 2` 幾乎等價於 `(l + r) // 2`？

兩者數學上等價，因為：
- `l + (r - l) / 2 = (2l + r - l) / 2 = (l + r) / 2`

**舉例：**
假設 `l = 10`，`r = 20`：
- `(l + r) // 2 = (10 + 20) // 2 = 30 // 2 = 15`
- `l + (r - l) // 2 = 10 + (20 - 10) // 2 = 10 + 10 // 2 = 10 + 5 = 15`

所以兩者結果相同。但當 `l` 和 `r` 很大時，`l + r` 可能溢位，`l + (r - l) / 2` 則不會。

---
