# 206. Reverse Linked List

> 難度：Easy 🟢

> 題型：Linked List

## 題目描述
給定一個單向鏈結串列的頭節點 head，請反轉該鏈結串列，並回傳反轉後的頭節點。

> Given the head of a singly linked list, reverse the list, and return the reversed list.

---

## 💡 解題思路

### Two Pointers（雙指標迴圈法）
1. 初始化一個 prev 指標為 None，curr 指向 head。
2. 迴圈遍歷鏈結串列：
   - 暫存 curr.next。
   - 將 curr.next 指向 prev，實現反轉。
   - prev 前進到 curr，curr 前進到下一個節點。
3. 迴圈結束後，prev 即為反轉後的新頭節點。

> ⚠️ 注意：反轉過程需小心指標操作，避免節點遺失。

### 遞迴法
1. 遞迴到鏈結串列的尾端（head 為 None 或 head.next 為 None）。
2. 回傳時將 head.next 的 next 指向 head，將 head.next 設為 None，實現反轉。
3. 每層遞迴都將子串列反轉，最終回傳新的頭節點。

> ⚠️ 注意：遞迴需理解指標的回傳與斷開，避免形成環狀鏈結。

---

## 🔍 演算法與資料結構分析

### Two Pointers（雙指標迴圈法）
| 項目         | 說明                        |
|--------------|-----------------------------|
| 使用資料結構 | 單向鏈結串列                |
| 時間複雜度   | O(n)                        |
| 空間複雜度   | O(1)                        |
| 優點         | 原地反轉，無需額外空間      |
| 缺點         | 需小心指標操作，易出錯      |

### 遞迴法
| 項目         | 說明                        |
|--------------|-----------------------------|
| 使用資料結構 | 單向鏈結串列                |
| 時間複雜度   | O(n)                        |
| 空間複雜度   | O(n)（遞迴呼叫堆疊）        |
| 優點         | 程式碼簡潔，遞迴思路清晰    |
| 缺點         | 額外遞迴堆疊空間，過深可能導致 stack overflow |

---

## ⚡ 程式碼實作（Python）

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val              # 節點的值
        self.next = next            # 下一個節點

def reverseList(head: ListNode) -> ListNode:
    prev = None                    # 前一個節點初始化為 None
    curr = head                    # 當前節點初始化為 head
    while curr:                    # 當前節點不為 None 時進行迴圈
        next_temp = curr.next      # 暫存下一個節點
        curr.next = prev           # 將當前節點的 next 指向前一個節點
        prev = curr                # prev 前進到 curr
        curr = next_temp           # curr 前進到下一個節點
    return prev                    # prev 為反轉後的新頭節點
```

---

## ⚡ 遞迴解法（Python）

```python
# 遞迴方式反轉鏈結串列
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val              # 節點的值
        self.next = next            # 下一個節點

def reverseListRecursive(head: ListNode) -> ListNode:
    if not head or not head.next:   # 遞迴終止條件：空節點或最後一個節點
        return head                 # 回傳最後一個節點作為新頭
    new_head = reverseListRecursive(head.next)  # 遞迴反轉後續節點
    head.next.next = head           # 將下一個節點的 next 指回自己
    head.next = None                # 斷開原本的 next 連結
    return new_head                 # 回傳新的頭節點
```
