# 23. Merge k Sorted Lists

> 難度：Hard 🔴

> 題型：Linked List、Divide and Conquer

## 題目描述
> 給定一個包含 k 個已排序鏈結串列的陣列 lists，每個鏈結串列皆已按升序排序。
> 請將所有鏈結串列合併為一個排序後的鏈結串列，並返回合併後的鏈結串列。

> You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
> Merge all the linked-lists into one sorted linked-list and return it.

---

## 💡 解題思路
1. 採用「兩兩合併」的方式，每次將兩個已排序的鏈結串列合併成一個新串列。
2. 將合併後的新串列收集起來，重複進行兩兩合併，直到只剩下一個串列。
3. 合併兩個已排序鏈結串列可用雙指針法，逐步比較節點值。
4. 時間複雜度優於直接串接所有節點再排序。

> ⚠️ 若 lists 為空或所有串列皆為空，直接回傳 None。

---

## 📚 範例

| 輸入 | 輸出 |
|------|------|
| lists = [[1,4,5],[1,3,4],[2,6]] | 1->1->2->3->4->4->5->6 |
| lists = [] | None |
| lists = [[]] | None |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                                      |
|--------------|-------------------------------------------|
| 使用資料結構 | 鏈結串列 (Linked List)                    |
| 時間複雜度   | O(N log k)，N 為總節點數，k 為串列數量     |
| 空間複雜度   | O(1)（不含輸出所需空間）                  |
| 優點         | 不需額外排序，效率高，適合大量串列合併     |
| 缺點         | 若 k 很大，遞迴或迴圈層數較多              |

---

## 🧑‍💻 程式碼（Python，含註解）

```python
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # 節點的值
        self.next = next  # 下一個節點

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # 建立虛擬頭節點
        tail = dummy  # 指向合併後串列的尾端
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1  # l1 較小，接到尾端
                l1 = l1.next  # l1 往後移
            else:
                tail.next = l2  # l2 較小，接到尾端
                l2 = l2.next  # l2 往後移
            tail = tail.next  # 尾端往後移
        tail.next = l1 if l1 else l2  # 接上剩餘節點
        return dummy.next  # 回傳合併後的頭節點

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None  # 空串列直接回傳 None
        while len(lists) > 1:
            merged = []  # 存放合併後的串列
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged.append(self.mergeTwoLists(l1, l2))  # 兩兩合併
            lists = merged  # 更新 lists
        return lists[0]  # 回傳最終合併結果
```

---
