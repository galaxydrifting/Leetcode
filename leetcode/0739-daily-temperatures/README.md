# 739. Daily Temperatures

> 難度：Medium 🟡

> 題型：Stack & Array

## 題目描述
> 給定一個整數陣列 `temperatures`，代表每日的氣溫，請回傳一個陣列 `answer`，其中 `answer[i]` 表示在第 i 天之後，必須等幾天才會遇到更高的氣溫。如果之後都不會有更高的氣溫，則 `answer[i]` 設為 0。

> Given an array of integers `temperatures` representing the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

---

## 💡 解題思路
1. 使用單調遞減堆疊（stack）來追蹤尚未遇到更高溫度的索引。
2. 從左到右遍歷 `temperatures`，每遇到比堆疊頂端索引所指溫度還高的溫度時，彈出堆疊並計算等待天數。
3. 若堆疊為空或當前溫度不高於堆疊頂端，則將當前索引壓入堆疊。
4. 最後堆疊中剩下的索引，其對應 `answer` 值保持為 0。

> ⚠️ 本題關鍵在於利用 stack 快速找到下一個更高溫度的位置，避免暴力雙迴圈導致 O(n^2) 時間複雜度。

---

## 📚 範例

| 輸入                | 輸出         |
|---------------------|--------------|
| [73,74,75,71,69,72,76,73] | [1,1,4,2,1,1,0,0] |
| [30,40,50,60]       | [1,1,1,0]    |
| [30,60,90]          | [1,1,0]      |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                        |
|--------------|-----------------------------|
| 使用資料結構 | Stack（堆疊）               |
| 時間複雜度   | O(n)                        |
| 空間複雜度   | O(n)                        |
| 優點         | 單次遍歷即可完成，效率高     |
| 缺點         | 需額外 stack 空間            |

---

## ⚡ 程式碼實作（Python）

```python
from typing import List

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    answer = [0] * n
    stack = []  # 存放索引
    for i, temp in enumerate(temperatures):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop()
            answer[prev_index] = i - prev_index
        stack.append(i)
    return answer
```
