# 146. LRU Cache
# solution.py
# 實作最近最少使用快取（LRU Cache）

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
