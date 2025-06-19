# 2. Add Two Numbers

> 難度：Medium 🟡

> 題型：Linked List

## 題目描述
> 給定兩個非空的鏈結串列，分別代表兩個非負整數，數字以逆序儲存，每個節點只存一位數。請將兩數相加，並以相同形式（逆序鏈結串列）回傳其和。

> You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

> 你可以假設這兩個數字除了數字 0 本身之外，沒有任何前導零。

---

## 💡 解題思路
1. 使用虛擬頭節點（dummy node）簡化鏈結串列操作。
2. 同步遍歷兩個鏈結串列，逐位相加，並考慮進位（carry）。
3. 每次相加後建立新節點，將餘數存入。
4. 若有進位需額外補一節點。
5. 最後回傳虛擬頭節點的 next。

> ⚠️ 注意：兩個鏈結串列長度可能不同，需處理長度不一與進位的情況。

---

## 📚 範例

| 輸入           | 輸出    |
|----------------|---------|
| [2,4,3], [5,6,4] | [7,0,8] |
| [0], [0]         | [0]     |
| [9,9,9,9,9,9,9], [9,9,9,9] | [8,9,9,9,0,0,0,1] |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                                  |
|--------------|---------------------------------------|
| 使用資料結構 | 鏈結串列（Linked List）               |
| 時間複雜度   | O(max(m, n))，m, n 為兩串列長度       |
| 空間複雜度   | O(max(m, n))，需新建結果鏈結串列      |
| 優點         | 可處理任意長度、進位，無需反轉串列     |
| 缺點         | 需額外空間儲存結果                    |

---

## 🧑‍💻 程式碼（Python，含註解）

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # 節點的值
        self.next = next  # 下一個節點

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()  # 建立虛擬頭節點，方便操作
        current = dummy     # 指標指向目前節點
        carry = 0           # 進位初始為 0
        while l1 or l2 or carry:  # 只要有一個不為空或有進位就繼續
            val1 = l1.val if l1 else 0  # 取 l1 的值，若為空則為 0
            val2 = l2.val if l2 else 0  # 取 l2 的值，若為空則為 0
            total = val1 + val2 + carry  # 計算總和
            carry = total // 10          # 更新進位
            current.next = ListNode(total % 10)  # 新節點存餘數
            current = current.next  # 移動指標
            if l1:
                l1 = l1.next  # l1 前進
            if l2:
                l2 = l2.next  # l2 前進
        return dummy.next  # 回傳結果鏈結串列的頭節點
```

---
