# 853. Car Fleet

> 難度：Medium 🟡

> 題型：Stack, Sorting, Simulation

## 題目描述
> 有 n 輛車分別位於距離起點 0 英里處的不同位置，目標是到達終點 target 英里。
> 
> 給定兩個整數陣列 position 和 speed，長度皆為 n，position[i] 代表第 i 輛車的起始位置，speed[i] 代表其速度（英里/小時）。
> 
> 車輛不能超車，但可以追上前方車輛並以較慢速度同行。
> 
> 一個「車隊」是指一輛或多輛車並排行駛，車隊的速度為其中最慢車輛的速度。
> 
> 若某車在終點追上車隊，仍視為同一車隊。
> 
> 請回傳最終能到達終點的車隊數量。
>
> ---
>
> There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.
>
> You are given two integer array position and speed, both of length n, where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.
>
> A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
>
> A car fleet is a car or cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.
>
> If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.
>
> Return the number of car fleets that will arrive at the destination.

---

## 💡 解題思路
1. 將所有車輛依照起始位置由遠到近排序（離終點越近的車排前面）。
2. 計算每輛車到達終點所需時間：`(target - position) / speed`。
3. 從最接近終點的車開始，若後方車輛到達終點所需時間較短，則會追上前方車隊，否則形成新車隊。
4. 使用 stack 模擬車隊合併過程，最後 stack 長度即為車隊數量。

> ℹ️ 注意：若有多輛車同時到達終點，仍視為同一車隊。

---

## 📚 範例

| 輸入 | 輸出 |
|------|------|
| target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3] | 3 |
| target = 10, position = [3], speed = [3] | 1 |
| target = 100, position = [0,2,4], speed = [4,2,1] | 1 |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                                  |
|--------------|---------------------------------------|
| 使用資料結構 | Stack, Array, Sorting                 |
| 時間複雜度   | O(n log n)（排序）                    |
| 空間複雜度   | O(n)（儲存時間與 stack）              |
| 優點         | 模擬直觀、易於理解                    |
| 缺點         | 需額外空間儲存排序與 stack            |

---

## ⚡ 程式碼實作（Python）

```python
from typing import List

def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    # 將車輛依照起始位置由遠到近排序
    cars = sorted(zip(position, speed), reverse=True)
    stack = []
    for pos, spd in cars:
        time = (target - pos) / spd
        if not stack or time > stack[-1]:
            stack.append(time)
        # 若 time <= stack[-1]，代表會追上前方車隊，無需新增
    return len(stack)
```
