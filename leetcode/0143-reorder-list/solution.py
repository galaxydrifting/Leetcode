# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # 節點的值
        self.next = next  # 下一個節點


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 步驟1: 使用快慢指針找到中點
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next  # 慢指針每次走一步
            fast = fast.next.next  # 快指針每次走兩步
        # 步驟2: 反轉後半段鏈結串列
        prev, curr = None, slow.next
        slow.next = None  # 斷開前後兩段
        while curr:
            next_temp = curr.next  # 暫存下一個節點
            curr.next = prev  # 指向前一個節點
            prev = curr  # 前移 prev
            curr = next_temp  # 前移 curr
        # 步驟3: 交錯合併兩段
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next  # 暫存下一個節點
            first.next = second  # 前段指向後段
            second.next = tmp1  # 後段指向前段下一個
            first, second = tmp1, tmp2  # 前移指標


# 範例測試
if __name__ == "__main__":
    def print_list(node):
        res = []
        while node:
            res.append(str(node.val))
            node = node.next
        print("→".join(res))

    # 建立測試鏈結串列 1→2→3→4→5
    n5 = ListNode(5)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)
    print("原始串列：", end="")
    print_list(n1)
    Solution().reorderList(n1)
    print("重排後：", end="")
    print_list(n1)
