# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # 節點的值
        self.next = next  # 下一個節點

# 判斷連結串列是否有環
# head: ListNode，連結串列的頭節點
# 回傳: bool，若有環則回傳 True，否則回傳 False


def hasCycle(head):
    # 使用快慢指針法
    slow = head  # 慢指針，每次走一步
    fast = head  # 快指針，每次走兩步
    while fast and fast.next:
        slow = slow.next         # 慢指針走一步
        fast = fast.next.next   # 快指針走兩步
        if slow == fast:
            # 快慢指針相遇，表示有環
            return True
    # 快指針遇到 None，表示無環
    return False


# 範例測試
if __name__ == "__main__":
    # 建立一個有環的連結串列: 3 -> 2 -> 0 -> -4 -> (回到2)
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # 建立環
    print(f"測試1: {hasCycle(node1)} (預期: True)")

    # 建立一個無環的連結串列: 1 -> 2
    node5 = ListNode(1)
    node6 = ListNode(2)
    node5.next = node6
    print(f"測試2: {hasCycle(node5)} (預期: False)")

    # 單一節點，無環
    node7 = ListNode(1)
    print(f"測試3: {hasCycle(node7)} (預期: False)")
