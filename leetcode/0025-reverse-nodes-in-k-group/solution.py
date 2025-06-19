from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # 節點的值
        self.next = next  # 下一個節點的指標

    def __repr__(self):
        return f"{self.val}->{self.next}" if self.next else f"{self.val}"

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 建立虛擬頭節點，方便處理頭部反轉
        dummy = ListNode(0, head)  # dummy.next 指向 head
        groupPrev = dummy  # groupPrev 指向每組反轉前的前一個節點

        while True:
            # 找到本組的第 k 個節點
            kth = self.getKth(groupPrev, k)  # kth 為本組的最後一個節點
            if not kth:
                break  # 不足 k 個節點，結束
            groupNext = kth.next  # 記錄下一組的起點

            # 反轉本組節點
            prev, curr = kth.next, groupPrev.next  # prev 指向下一組的頭，curr 指向本組的頭
            while curr != groupNext:
                tmp = curr.next  # 暫存下一個節點
                curr.next = prev  # 指向前一個節點（反轉）
                prev = curr  # prev 前移
                curr = tmp  # curr 前移

            # 連接反轉後的節點
            tmp = groupPrev.next  # 記錄本組反轉前的頭（反轉後變尾）
            groupPrev.next = kth  # 前一組的尾接到本組反轉後的頭
            groupPrev = tmp  # groupPrev 移到本組反轉後的尾
        return dummy.next  # 返回新頭節點

    def getKth(self, curr: ListNode, k: int) -> Optional[ListNode]:
        # 往後走 k 步，找到第 k 個節點
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

# 工具函數：將 list 轉為 linked list
def list_to_linkedlist(lst: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)  # 虛擬頭節點
    curr = dummy  # 當前節點
    for val in lst:
        curr.next = ListNode(val)  # 新建節點
        curr = curr.next  # 移動到新節點
    return dummy.next  # 返回真正的頭節點

# 工具函數：將 linked list 轉為 list
def linkedlist_to_list(head: Optional[ListNode]) -> List[int]:
    res = []  # 結果列表
    while head:
        res.append(head.val)  # 加入當前節點值
        head = head.next  # 移動到下一個節點
    return res

# 範例測試
if __name__ == "__main__":
    sol = Solution()  # 建立 Solution 物件
    # 測試用例 1
    head1 = list_to_linkedlist([1,2,3,4,5])  # 建立連結串列
    k1 = 2
    result1 = sol.reverseKGroup(head1, k1)  # 執行反轉
    print("Example 1:", linkedlist_to_list(result1))  # 輸出結果

    # 測試用例 2
    head2 = list_to_linkedlist([1,2,3,4,5])
    k2 = 3
    result2 = sol.reverseKGroup(head2, k2)
    print("Example 2:", linkedlist_to_list(result2))
