# 150. Evaluate Reverse Polish Notation

> 難度：Medium 🟡

> 題型：Stack

## 題目描述
> 給定一個字串陣列 tokens，代表一個以逆波蘭表示法（Reverse Polish Notation, RPN）寫成的算術運算式，請計算其值並回傳整數結果。

> You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation. Evaluate the expression. Return an integer that represents the value of the expression.

- 有效運算子為 '+', '-', '*', '/'。
- 每個運算元可能是整數或另一個運算式。
- 除法結果需向零截斷。
- 不會有除以零的情況。
- 輸入一定是有效的逆波蘭表示式。
- 所有運算結果皆可用 32 位元整數表示。

---

## 💡 解題思路
1. 建立一個堆疊（stack）用來存放運算元。
2. 依序遍歷 tokens：
   - 若為數字，轉為整數後推入堆疊。
   - 若為運算子，從堆疊彈出兩個數字，依運算子計算後再推回堆疊。
3. 最後堆疊剩下的即為答案。

> ⚠️ 注意：除法時需使用 int(a / b) 以符合向零截斷。

---

## 📚 範例

| 輸入 | 輸出 |
|------|------|
| ["2","1","+","3","*"] | 9 |
| ["4","13","5","/","+"] | 6 |
| ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] | 22 |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                |
|--------------|---------------------|
| 使用資料結構 | Stack（堆疊）       |
| 時間複雜度   | O(n)                |
| 空間複雜度   | O(n)                |
| 優點         | 實作簡單，直觀      |
| 缺點         | 需額外堆疊空間      |

---

## ⚡ 程式碼實作（Python）

```python
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:  # '/'
                    stack.append(int(a / b))  # 向零截斷
        return stack[0]
```
