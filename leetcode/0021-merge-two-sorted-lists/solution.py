# 21. Merge Two Sorted Lists
# Easy
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

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
