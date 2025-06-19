# 0023. Merge k Sorted Lists - 兩兩合併法
# 題目要求：合併 k 個已排序的鏈結串列，回傳合併後的排序鏈結串列
# 每行皆有中文註解

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # 節點的值
        self.next = next  # 下一個節點

    def __str__(self):
        # 方便 debug，將鏈結串列轉為字串
        result = []
        node = self
        while node:
            result.append(str(node.val))
            node = node.next
        return '->'.join(result)

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 合併兩個已排序的鏈結串列
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
        # 兩兩合併，直到只剩一個串列
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

# 範例測試程式進入點
if __name__ == "__main__":
    # 建立測試用的鏈結串列
    def build_list(arr):
        dummy = ListNode()
        curr = dummy
        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next

    # 測試資料
    lists = [build_list([1,4,5]), build_list([1,3,4]), build_list([2,6])]
    # 執行合併
    sol = Solution()
    result = sol.mergeKLists(lists)
    # 輸出結果
    if result:
        print(result)  # 預期輸出：1->1->2->3->4->4->5->6
    else:
        print("None")
