# 981. Time Based Key-Value Store

> 難度：Medium 🟡

> 題型：Design & Hash Table & Binary Search

## 題目描述
設計一個時間型 key-value 資料結構，可以在不同時間點為同一個 key 儲存多個值，並能在指定時間點查詢該 key 的值。

> Design a time-based key-value data structure that can store multiple values for the same key at different timestamps and retrieve the key’s value at a certain timestamp.

---

## 💡 解題思路
1. 使用字典（hash map）儲存每個 key 對應的 (timestamp, value) 列表。
2. set 時，將 (timestamp, value) 加入對應 key 的列表（保證 timestamp 遞增）。
3. get 時，對該 key 的 timestamp 列表進行二分搜尋，找出小於等於目標 timestamp 的最大 timestamp，回傳對應 value。
4. 若找不到符合條件的 timestamp，回傳空字串。

> ⚠️ 注意：timestamp 保證遞增，適合用二分搜尋加速查找。

---

## 📚 範例

| 操作                | 輸入參數                | 輸出   |
|---------------------|-------------------------|--------|
| set("foo", "bar", 1) | -                      | -      |
| get("foo", 1)        | -                      | "bar"  |
| get("foo", 3)        | -                      | "bar"  |
| set("foo", "bar2", 4)| -                      | -      |
| get("foo", 4)        | -                      | "bar2" |
| get("foo", 5)        | -                      | "bar2" |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                                      |
|--------------|-------------------------------------------|
| 使用資料結構 | 字典（hash map）+ 每個 key 對應的有序列表 |
| 時間複雜度   | set: O(1)，get: O(log n)                  |
| 空間複雜度   | O(N)，N 為所有 set 操作次數               |
| 優點         | 查詢效率高，適合大量查詢                   |
| 缺點         | 需額外儲存所有歷史資料，佔用較多空間       |

---

## ⚡ 程式碼實作（Python）

```python
from collections import defaultdict
# import bisect  # 面試時建議不用，可作為補充

class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)  # 用 dict 儲存每個 key 的 (timestamp, value) 列表

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))  # 直接 append，timestamp 遞增

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""  # 若 key 不存在，回傳空字串
        arr = self.store[key]
        # 手動二分搜尋，找最大且 <= timestamp 的 timestamp
        left, right = 0, len(arr) - 1
        res = ""
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]  # 更新答案，繼續往右找
                left = mid + 1
            else:
                right = mid - 1
        return res
        # --- 補充：若允許使用 bisect 模組，可用下列寫法 ---
        # i = bisect.bisect_right(arr, (timestamp, chr(127)))
        # if i == 0:
        #     return ""
        # return arr[i-1][1]

if __name__ == "__main__":
    kv = TimeMap()
    kv.set("foo", "bar", 1)
    print(kv.get("foo", 1))   # 輸出 "bar"
    print(kv.get("foo", 3))   # 輸出 "bar"
    kv.set("foo", "bar2", 4)
    print(kv.get("foo", 4))   # 輸出 "bar2"
    print(kv.get("foo", 5))   # 輸出 "bar2"
```
