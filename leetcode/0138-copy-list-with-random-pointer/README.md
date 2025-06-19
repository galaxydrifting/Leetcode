# 138. Copy List with Random Pointer

> 難度：Medium 🟡

> 題型：Linked List

## 題目描述
> 給定一個長度為 n 的鏈結串列，每個節點除了有 next 指標外，還有一個 random 指標，random 可以指向串列中的任意節點或為 null。
> 
> 請你建立這個串列的深拷貝（deep copy），也就是建立一個全新的串列，讓新串列的每個節點值與原串列相同，且 next 與 random 指標的結構完全一致，但新串列的節點不能指向原串列的任何節點。
>
> The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
> - val: an integer representing Node.val
> - random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

---

## 💡 解題思路
1. 先遍歷原串列，複製每個節點，並用一個哈希表記錄原節點與新節點的對應關係。
2. 再次遍歷原串列，根據哈希表設定新節點的 next 與 random 指標。
3. 回傳新串列的頭節點。

> ⚠️ 注意：random 指標可能為 null，也可能指向自己或其他任意節點。

---

## 📚 範例

| 輸入 | 輸出 |
|------|------|
| [[7,null],[13,0],[11,4],[10,2],[1,0]] | [[7,null],[13,0],[11,4],[10,2],[1,0]] |
| [[1,1],[2,1]] | [[1,1],[2,1]] |
| [[3,null],[3,0],[3,null]] | [[3,null],[3,0],[3,null]] |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                |
|--------------|---------------------|
| 使用資料結構 | 雙指標、哈希表      |
| 時間複雜度   | O(n)                |
| 空間複雜度   | O(n)                |
| 優點         | 直觀、易於理解      |
| 缺點         | 額外空間需求        |

---

## 🧑‍💻 程式碼（Python，含註解）

```python
# 定義 Node 類別
class Node:
    def __init__(self, val: int, next: 'Node' = None, random: 'Node' = None):
        self.val = val  # 節點值
        self.next = next  # 下一個節點
        self.random = random  # 隨機指標

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
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
```

---
