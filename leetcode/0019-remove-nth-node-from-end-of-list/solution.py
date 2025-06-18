# 題目：移除連結串列的倒數第 N 個節點
# LeetCode 19. Remove Nth Node From End of List
# 時間複雜度 O(L)，空間複雜度 O(1)

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # 節點值
        self.next = next  # 下一個節點

    def __str__(self):
        # 方便 debug，將連結串列轉為字串
        result = []
        node = self
        while node:
            result.append(str(node.val))
            node = node.next
        return '->'.join(result)


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    移除連結串列的倒數第 n 個節點
    """
    dummy = ListNode(0, head)  # 建立虛擬頭節點，方便處理邊界情況
    fast = slow = dummy  # 快慢指針都從 dummy 開始

    # 快指針先走 n 步
    for _ in range(n):
        fast = fast.next  # ...快指針前進...

    # 快慢指針一起走，直到快指針到尾端
    while fast.next:
        fast = fast.next  # ...快指針前進...
        slow = slow.next  # ...慢指針前進...

    # 慢指針的下一個節點就是要被移除的節點
    slow.next = slow.next.next  # ...移除節點...
    return dummy.next  # 返回新的頭節點


# 範例測試
if __name__ == "__main__":
    # 建立連結串列 1->2->3->4->5
    n5 = ListNode(5)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)
    head = n1
    print("原始連結串列:", head)
    n = 2
    new_head = removeNthFromEnd(head, n)
    print(f"移除倒數第 {n} 個節點後:", new_head)
