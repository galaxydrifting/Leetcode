# 22. Generate Parentheses

> 難度：Medium 🟡

> 題型：Backtracking & Recursion

## 題目描述
> 給定 n 對括號，請寫一個函數產生所有合法的括號組合。

> Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

---

## 💡 解題思路
1. 使用回溯法（Backtracking）遞迴生成所有可能的括號組合。
2. 維護左右括號剩餘數量，只有當左括號還有剩時才能加左括號，右括號剩餘數量大於左括號時才能加右括號。
3. 當左右括號都用完時，將組合加入結果。

> ⚠️ 注意：每次遞迴時都要確保組合合法，避免產生不合法的括號序列。

---

## 📚 範例

| 輸入 | 輸出 |
|------|------|
| n = 3 | ["((()))","(()())","(())()","()(())","()()()"] |
| n = 1 | ["()"] |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                                  |
|--------------|---------------------------------------|
| 使用資料結構 | 遞迴、字串、陣列                     |
| 時間複雜度   | O(4^n / sqrt(n))                      |
| 空間複雜度   | O(4^n / sqrt(n))（遞迴樹與結果儲存）  |
| 優點         | 能產生所有合法組合，易於理解與實作    |
| 缺點         | 當 n 較大時，組合數量指數成長         |

---

## ⚡ 程式碼實作（Python）

```python
from typing import List

def generateParenthesis(n: int) -> List[str]:
    res = []
    def backtrack(s='', left=0, right=0):
        if len(s) == 2 * n:
            res.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)
    backtrack()
    return res
```
