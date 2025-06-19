# 138. Copy List with Random Pointer
# 題目：複製帶隨機指標的鏈結串列
# LeetCode: https://leetcode.com/problems/copy-list-with-random-pointer/

from typing import Optional


class Node:
    def __init__(self, val: int, next: 'Optional[Node]' = None, random: 'Optional[Node]' = None):
        self.val = val  # 節點值
        self.next = next  # 下一個節點
        self.random = random  # 隨機指標

    def __repr__(self):
        # 方便 debug，顯示節點值與 random 指向的值
        random_val = self.random.val if self.random else None
        return f"Node(val={self.val}, random={random_val})"


def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
    """
    複製帶隨機指標的鏈結串列
    :param head: 原始鏈結串列的頭節點
    :return: 新鏈結串列的頭節點
    """
    if not head:
        return None  # 若原串列為空，直接回傳 None

    old_to_new = dict()  # 哈希表：原節點 -> 新節點
    cur = head
    # 第一次遍歷：複製所有節點
    while cur:
        old_to_new[cur] = Node(cur.val)  # 建立新節點並記錄對應關係
        cur = cur.next  # 移動到下一個節點

    cur = head
    # 第二次遍歷：設定 next 與 random
    while cur:
        old_to_new[cur].next = old_to_new.get(cur.next)  # 設定 next
        old_to_new[cur].random = old_to_new.get(cur.random)  # 設定 random
        cur = cur.next  # 移動到下一個節點

    return old_to_new[head]  # 回傳新串列的頭節點

# ===== 範例測試程式 =====


def build_linked_list(data):
    """
    根據輸入的 [val, random_index] 格式建立鏈結串列
    :param data: List[List[int, Optional[int]]]
    :return: Node
    """
    if not data:
        return None
    nodes = [Node(val) for val, _ in data]  # 先建立所有節點
    for idx, (_, random_idx) in enumerate(data):
        if idx < len(nodes) - 1:
            nodes[idx].next = nodes[idx + 1]  # 設定 next
        if random_idx is not None:
            nodes[idx].random = nodes[random_idx]  # 設定 random
    return nodes[0]


def print_linked_list(head):
    """
    以 [val, random_index] 格式輸出鏈結串列
    """
    nodes = []
    node_to_index = dict()
    cur = head
    idx = 0
    while cur:
        node_to_index[cur] = idx
        nodes.append(cur)
        cur = cur.next
        idx += 1
    res = []
    for node in nodes:
        random_idx = node_to_index[node.random] if node.random else None
        res.append([node.val, random_idx])
    print(res)


if __name__ == "__main__":
    # 範例 1
    data1 = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    head1 = build_linked_list(data1)
    copied1 = copyRandomList(head1)
    print("原始:")
    print_linked_list(head1)
    print("複製:")
    print_linked_list(copied1)

    # 範例 2
    data2 = [[1, 1], [2, 1]]
    head2 = build_linked_list(data2)
    copied2 = copyRandomList(head2)
    print("原始:")
    print_linked_list(head2)
    print("複製:")
    print_linked_list(copied2)

    # 範例 3
    data3 = [[3, None], [3, 0], [3, None]]
    head3 = build_linked_list(data3)
    copied3 = copyRandomList(head3)
    print("原始:")
    print_linked_list(head3)
    print("複製:")
    print_linked_list(copied3)
