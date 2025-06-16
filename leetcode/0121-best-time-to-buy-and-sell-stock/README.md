# 121. Best Time to Buy and Sell Stock

> 難度：Easy 🟢

> 題型：Array & Sliding Window

## 題目描述
> 給定一個整數陣列 prices，prices[i] 代表第 i 天的股票價格。
> 你只能選擇一天買入股票，並選擇在未來的某一天賣出，請回傳你能獲得的最大利潤。如果無法獲利，請回傳 0。

> You are given an array prices where prices[i] is the price of a given stock on the ith day.
> You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
> Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

---

## 💡 解題思路
1. 使用 two pointers（sliding window）方法：left 指向買入日，right 指向賣出日。
2. 初始 left=0，right=1，遍歷陣列。
3. 若 prices[right] > prices[left]，計算利潤並更新最大值。
4. 若 prices[right] <= prices[left]，將 left 移到 right（代表找到更低的買入價）。
5. 持續移動 right，直到遍歷完整個陣列。
6. 回傳最大利潤。

> ⚠️ 注意：只能買賣一次，且賣出日必須在買入日之後。

---

## 📚 範例

| 輸入           | 輸出 |
|----------------|------|
| [7,1,5,3,6,4]  | 5    |
| [7,6,4,3,1]    | 0    |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                |
|--------------|---------------------|
| 使用資料結構 | 陣列、雙指標        |
| 時間複雜度   | O(n)                |
| 空間複雜度   | O(1)                |
| 優點         | 一次遍歷、效率高    |
| 缺點         | 只適用於一次買賣    |

---

## ⚡ 程式碼實作（Python）

```python
# 使用 sliding window 解法，逐行加上中文註解
from typing import List

def maxProfit(prices: List[int]) -> int:
    max_profit = 0  # 最大利潤初始為 0
    left = 0        # left 指標，代表買入日
    # 遍歷每一天，right 指標代表賣出日
    for right in range(1, len(prices)):
        if prices[right] > prices[left]:  # 若賣出價高於買入價
            profit = prices[right] - prices[left]  # 計算利潤
            max_profit = max(max_profit, profit)   # 更新最大利潤
        else:
            left = right  # 若遇到更低價，更新買入日
    return max_profit  # 回傳最大利潤

if __name__ == "__main__":
    # 範例測試
    print(maxProfit([7,1,5,3,6,4]))  # 輸出 5
    print(maxProfit([7,6,4,3,1]))    # 輸出 0
```
