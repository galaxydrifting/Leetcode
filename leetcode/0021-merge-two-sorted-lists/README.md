# 21. Merge Two Sorted Lists

> 題型：Linked List

> 難度：Easy 🟢

## 題目描述
> You are given the heads of two sorted linked lists list1 and list2.
> Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
> Return the head of the merged linked list.
>
> 給定兩個已排序的鏈結串列 list1 和 list2，請將它們合併為一個新的已排序鏈結串列，並回傳新串列的頭節點。

---

## 💡 解題思路
1. 使用虛擬頭節點（dummy node）簡化操作。
2. 依序比較兩個串列的當前節點，將較小的節點接到新串列後。
3. 其中一個串列用盡後，直接將另一個串列剩餘部分接上。

> ⚠️ 注意：要正確處理串列為空的情況。

---

## 📚 範例

| 輸入 | 輸出 |
|-----------------------------|----------------|
| list1 = [1,2,4], list2 = [1,3,4] | [1,1,2,3,4,4] |
| list1 = [], list2 = []            | []           |
| list1 = [], list2 = [0]           | [0]          |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                |
|--------------|---------------------|
| 使用資料結構 | 鏈結串列（Linked List）|
| 時間複雜度   | O(n + m)            |
| 空間複雜度   | O(1)（不含輸出）    |
| 優點         | 原地合併，無需額外空間 |

---

## 🧑‍💻 Python 範例程式碼（含註解）

```python
from typing import Optional  # 匯入型別註解

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val        # 節點的值
        self.next = next      # 下一個節點

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()    # 建立虛擬頭節點，方便操作
        tail = dummy         # tail 指向新串列的最後一個節點
        while list1 and list2:  # 只要兩串列都還有節點
            if list1.val < list2.val:  # 比較當前節點值
                tail.next = list1      # 將較小節點接到新串列
                list1 = list1.next     # list1 往後移動
            else:
                tail.next = list2      # 將較小節點接到新串列
                list2 = list2.next     # list2 往後移動
            tail = tail.next           # tail 往後移動
        if list1:                      # 若 list1 尚有剩餘
            tail.next = list1          # 直接接上剩餘部分
        elif list2:                    # 若 list2 尚有剩餘
            tail.next = list2          # 直接接上剩餘部分
        return dummy.next              # 回傳合併後串列的頭節點
```
