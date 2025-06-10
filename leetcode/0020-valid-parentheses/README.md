# 0020. Valid Parentheses

> 難度：Easy 🟢

> 題型：Stack

## 題目描述
> 給定一個只包含 '(', ')', '{', '}', '[', ']' 的字串 s，請判斷輸入的字串是否為有效的括號組合。

>
> 有效字串需符合：
> 1. 開括號必須由相同類型的括號關閉。
> 2. 開括號必須以正確的順序關閉。
> 3. 每個關閉括號都必須有對應的開括號。
>
> Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
> 
> An input string is valid if:
> 1. Open brackets must be closed by the same type of brackets.
> 2. Open brackets must be closed in the correct order.
> 3. Every close bracket has a corresponding open bracket of the same type.

---

## 💡 解題思路
1. 使用堆疊（stack）來追蹤尚未配對的開括號。
2. 遍歷字串，遇到開括號就推入堆疊。
3. 遇到關括號時，檢查堆疊頂端是否為對應的開括號，若是則彈出，否則回傳 False。
4. 最後堆疊必須為空，才代表所有括號都正確配對。

> ⚠️ 若字串長度為奇數，一定不可能為有效括號。

---

## 📚 範例

| 輸入     | 輸出   |
|----------|--------|
| "()"     | True   |
| "()[]{}" | True   |
| "(]"     | False  |
| "([)]"   | False  |
| "{[]}"   | True   |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                |
|--------------|---------------------|
| 使用資料結構 | Stack（堆疊）       |
| 時間複雜度   | O(n)                |
| 空間複雜度   | O(n)                |
| 優點         | 實作簡單，效率高    |
| 缺點         | 僅適用於括號配對問題|

---

## ⚡ 程式碼實作（Python）

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                return False
        return not stack
```
