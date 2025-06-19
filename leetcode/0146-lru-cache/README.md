# 146. LRU Cache

> 難度：Medium 🟡

> 題型：Design, Hash Table, Linked List

## 題目描述
設計一個遵循最近最少使用（Least Recently Used, LRU）原則的快取（Cache）資料結構。

請實作 LRUCache 類別：
- `LRUCache(int capacity)` 以正整數作為容量初始化 LRU 快取。
- `int get(int key)` 如果 key 存在於快取中，回傳其值，否則回傳 -1。
- `void put(int key, int value)` 如果 key 已存在，更新其值；否則新增 key-value。若快取超過容量，移除最久未使用的 key。

> Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
>
> Implement the LRUCache class:
> - `LRUCache(int capacity)` Initialize the LRU cache with positive size capacity.
> - `int get(int key)` Return the value of the key if the key exists, otherwise return -1.
> - `void put(int key, int value)` Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
>
> The functions get and put must each run in O(1) average time complexity.

---

## 💡 解題思路
1. 使用雙向鏈結串列（Doubly Linked List）搭配哈希表（Hash Map）實現。
2. 哈希表用於 O(1) 查找節點，鏈結串列維護最近使用順序。
3. 每次 get/put 時，將該節點移到鏈結串列尾端（代表最近使用）。
4. put 時若超過容量，移除鏈結串列頭部（最久未使用）。

> ⚠️ 雙向鏈結串列需有虛擬頭尾節點，方便插入與刪除。

---

## 📚 範例

| 輸入 | 輸出 |
|------|------|
| ["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]] | [null,null,null,1,null,-1,null,-1,3,4] |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                                  |
|--------------|---------------------------------------|
| 使用資料結構 | 雙向鏈結串列 + 哈希表                 |
| 時間複雜度   | O(1)（get/put 均為常數時間）           |
| 空間複雜度   | O(capacity)                           |
| 優點         | 查找、插入、刪除皆為 O(1)              |
| 缺點         | 實作較複雜，需維護鏈結串列與哈希表同步 |

---

## 🧑‍💻 程式碼（Python，含註解）

```python
class Node:
    def __init__(self, key, val):
        self.key = key  # 節點的 key
        self.val = val  # 節點的值
        self.prev = None  # 前一個節點
        self.nxt = None   # 下一個節點

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity  # 快取容量
        self.cache = {}  # key 對應 Node 節點
        self.left = Node(0, 0)  # 虛擬頭節點，代表最久未使用（LRU）
        self.right = Node(0, 0)  # 虛擬尾節點，代表最近使用
        self.left.nxt, self.right.prev = self.right, self.left  # 初始化雙向鏈結串列
        
    def _remove(self, node):
        """從鏈結串列移除節點"""
        prev, nxt = node.prev, node.nxt  # 取得前後節點
        prev.nxt, nxt.prev = nxt, prev  # 斷開 node，前後節點互連

    def _insert(self, node):
        """將節點插入到鏈結串列尾端（最近使用）"""
        prev, nxt = self.right.prev, self.right  # 取得尾端前一節點與尾節點
        prev.nxt = nxt.prev = node  # 前一節點與尾節點都指向新節點
        node.prev = prev  # 新節點的 prev 指向前一節點
        node.nxt = self.right  # 新節點的 nxt 指向尾節點

    def get(self, key: int) -> int:
        if key in self.cache:  # 若 key 存在於快取
            self._remove(self.cache[key])  # 先移除原節點
            self._insert(self.cache[key])  # 再插入到尾端（最近使用）
            return self.cache[key].val  # 回傳值
        return -1  # 若不存在回傳 -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:  # 若 key 已存在
            self._remove(self.cache[key])  # 先移除舊節點
        self.cache[key] = Node(key, value)  # 建立新節點並放入快取
        self._insert(self.cache[key])  # 插入到尾端（最近使用）

        if len(self.cache) > self.cap:  # 若超過容量
            lru = self.left.nxt  # 取得最久未使用節點
            self._remove(lru)  # 從鏈結串列移除
            del self.cache[lru.key]  # 從快取刪除對應 key

# 範例測試
if __name__ == "__main__":
    lru = LRUCache(2)  # 建立容量為 2 的 LRUCache
    lru.put(1, 1)      # 快取為 {1=1}
    lru.put(2, 2)      # 快取為 {1=1, 2=2}
    print(lru.get(1))  # 回傳 1
    lru.put(3, 3)      # 移除 key 2，快取為 {1=1, 3=3}
    print(lru.get(2))  # 回傳 -1 (未找到)
    lru.put(4, 4)      # 移除 key 1，快取為 {4=4, 3=3}
    print(lru.get(1))  # 回傳 -1 (未找到)
    print(lru.get(3))  # 回傳 3
    print(lru.get(4))  # 回傳 4
```
