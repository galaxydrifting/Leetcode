# 347. Top K Frequent Elements

> 難度：Medium 🟡

> 題型：Heap & Hash Table

## 題目描述
> 給定一個整數陣列 nums 和一個整數 k，請回傳出現頻率前 k 高的元素。你可以以任意順序返回答案。

> Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

---

## 💡 解題思路
1. 使用雜湊表（Counter）統計每個元素出現的次數。
2. 直接利用 Counter.most_common(k) 取得出現頻率最高的 k 個元素。
3. 回傳這些元素作為答案。

> ℹ️ Counter.most_common(k) 可直接取得前 k 頻率元素，簡化實作。

---

## 📚 範例

| 輸入                | 輸出    |
|---------------------|---------|
| nums = [1,1,1,2,2,3], k = 2 | [1,2]   |
| nums = [1], k = 1           | [1]     |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                                  |
|--------------|---------------------------------------|
| 使用資料結構 | 雜湊表（Counter）                     |
| 時間複雜度   | O(N)                                  |
| 空間複雜度   | O(N)                                  |
| 優點         | 實作簡單，效率高                      |
| 缺點         | 需額外空間儲存計數                    |

---

## ⚡ 程式碼實作（Python）

```python
from collections import Counter
from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    # 直接用 Counter.most_common(k) 取得前 k 頻率元素
    return [item for item, _ in count.most_common(k)]
```
