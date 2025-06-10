# 155. Min Stack

> 難度：Medium 🟡

> 題型：Stack, Design

## 題目描述
> 設計一個支援 push、pop、top 以及在常數時間內檢索最小元素的堆疊。
>
> Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
>
> 你必須實作 MinStack 類別：
> - MinStack() 初始化堆疊物件。
> - void push(int val) 將元素 val 推入堆疊。
> - void pop() 移除堆疊頂端元素。
> - int top() 取得堆疊頂端元素。
> - int getMin() 檢索堆疊中的最小元素。
>
> 所有操作必須在 O(1) 時間內完成。

---

## 💡 解題思路
1. 使用兩個堆疊：主堆疊 stack 儲存所有元素，輔助堆疊 min_stack 儲存每一步的最小值。
2. push 時，同步將當前最小值推入 min_stack。
3. pop 時，兩個堆疊同時彈出。
4. top 直接回傳主堆疊頂端元素。
5. getMin 直接回傳 min_stack 頂端元素。

> ⚠️ min_stack 的頂端永遠是目前 stack 的最小值。

---

## 📚 範例

| 輸入 | 輸出 |
|------|------|
| ["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]] | [null,null,null,null,-3,null,0,-2] |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                |
|--------------|---------------------|
| 使用資料結構 | Stack（堆疊）       |
| 時間複雜度   | O(1)（所有操作）    |
| 空間複雜度   | O(n)                |
| 優點         | 所有操作皆為常數時間 |
| 缺點         | 需額外空間存輔助堆疊 |

---

## ⚡ 程式碼實作（Python）

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```
