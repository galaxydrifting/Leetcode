# 2. Add Two Numbers
# 題目要求：給定兩個非空的鏈結串列，分別代表兩個非負整數，數字以逆序儲存，每個節點只存一位數。
# 輸出兩數相加的結果（同樣以逆序儲存的鏈結串列）。

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # 節點的值
        self.next = next  # 下一個節點


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()  # 建立虛擬頭節點，方便操作
        current = dummy     # 指標指向目前節點
        carry = 0           # 進位初始為 0
        while l1 or l2 or carry:  # 只要有一個不為空或有進位就繼續
            val1 = l1.val if l1 else 0  # 取 l1 的值，若為空則為 0
            val2 = l2.val if l2 else 0  # 取 l2 的值，若為空則為 0
            total = val1 + val2 + carry  # 計算總和
            carry = total // 10          # 更新進位
            current.next = ListNode(total % 10)  # 新節點存餘數
            current = current.next  # 移動指標
            if l1:
                l1 = l1.next  # l1 前進
            if l2:
                l2 = l2.next  # l2 前進
        return dummy.next  # 回傳結果鏈結串列的頭節點

# 範例測試用：


def list_to_linkedlist(lst):
    """將 Python list 轉換為鏈結串列"""
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next


def linkedlist_to_list(node):
    """將鏈結串列轉換為 Python list"""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


if __name__ == "__main__":
    # 測試範例：342 + 465 = 807
    l1 = list_to_linkedlist([2, 4, 3])  # 代表數字 342
    l2 = list_to_linkedlist([5, 6, 4])  # 代表數字 465
    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)
    print(linkedlist_to_list(result))  # 預期輸出：[7,0,8]
