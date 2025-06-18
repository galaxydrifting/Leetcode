class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev

# 遞迴方式反轉鏈結串列


def reverseListRecursive(head: ListNode) -> ListNode:
    if not head or not head.next:   # 遞迴終止條件：空節點或最後一個節點
        return head                 # 回傳最後一個節點作為新頭
    new_head = reverseListRecursive(head.next)  # 遞迴反轉後續節點
    head.next.next = head           # 將下一個節點的 next 指回自己
    head.next = None                # 斷開原本的 next 連結
    return new_head                 # 回傳新的頭節點


def printList(head: ListNode):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(' > '.join(vals))


if __name__ == "__main__":
    # 建立範例 1->2->3
    n3 = ListNode(3)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)
    print("原始串列:")
    printList(n1)
    # Debug 遞迴反轉
    result = reverseListRecursive(n1)
    print("反轉後:")
    printList(result)
