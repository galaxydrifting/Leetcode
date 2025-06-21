# 297. Serialize and Deserialize Binary Tree

> 難度：Hard 🔴

> 題型：Tree、Design、DFS、BFS

## 題目描述
> Serialization 是將資料結構或物件轉換為位元序列，以便儲存於檔案、記憶體緩衝區，或透過網路傳輸，之後可於同一或不同環境還原。
> 
> 設計一個演算法來序列化（serialize）和反序列化（deserialize）二元樹。你可以自由設計序列化/反序列化的方式，只需確保能正確還原原始樹結構。

---

## 💡 解題思路
1. 使用前序遍歷（Preorder Traversal, DFS）將樹轉為字串，遇到空節點以特殊符號（如 #）標記。
2. 反序列化時，根據字串順序重建樹結構，遇到 # 則回傳 None。
3. 這種方式能完整保留樹的結構資訊，且實作簡單直觀。

### BFS（層序遍歷）作法
1. 使用佇列（Queue）進行層序遍歷，將每個節點值依序加入字串，空節點以 # 標記。
2. 反序列化時，依序取出字串中的值，利用佇列重建每一層的節點與其子節點。
3. BFS 作法更貼近 LeetCode 的序列化格式，適合處理完全二元樹或層級資訊。

> ⚠️ 注意：序列化與反序列化的格式需一致，且要處理空樹的情況。

---

## 📚 範例

| 輸入                | 輸出（DFS）           | 輸出（BFS）           |
|---------------------|----------------------|----------------------|
| root = [1,2,3,null,null,4,5] | '1,2,#,#,3,4,#,#,5,#,#' | '1,2,3,#,#,4,5,#,#,#,#' |

---

## 🔍 演算法與資料結構分析

| 項目         | DFS（遞迴）                | BFS（佇列）                |
|--------------|----------------------------|----------------------------|
| 使用資料結構 | 二元樹、字串、遞迴         | 二元樹、字串、佇列         |
| 時間複雜度   | O(N)（N 為節點數）         | O(N)（N 為節點數）         |
| 空間複雜度   | O(N)（遞迴與儲存序列化字串）| O(N)（佇列與序列化字串）   |
| 優點         | 邏輯簡單、易於實作與除錯   | 層級資訊明確、貼近 LeetCode|
| 缺點         | 產生的字串較長             | 空節點多時字串較長         |

---

## 🧑‍💻 Python 程式碼（含註解）

### DFS 實作
```python
# 定義二元樹節點類別
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # 節點值
        self.left = left  # 左子樹
        self.right = right  # 右子樹

class Codec:
    def serialize(self, root):
        """
        將二元樹序列化為字串（前序 DFS，使用 res list 收集）
        :type root: TreeNode
        :rtype: str
        """
        res = []  # 用來存放序列化結果
        def dfs(node):
            if not node:
                res.append("N")  # 空節點以 N 表示
                return
            res.append(str(node.val))  # 加入節點值
            dfs(node.left)  # 遞迴處理左子樹
            dfs(node.right)  # 遞迴處理右子樹
        dfs(root)
        return ",".join(res)  # 以逗號串接

    def deserialize(self, data):
        """
        將字串反序列化為二元樹（用 self.i 控制進度）
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")  # 拆分字串
        self.i = 0  # 指標
        def dfs():
            if vals[self.i] == "N":  # 遇到 N 表示空節點
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))  # 建立節點
            self.i += 1
            node.left = dfs()  # 遞迴建立左子樹
            node.right = dfs()  # 遞迴建立右子樹
            return node
        return dfs()

# 範例測試
if __name__ == "__main__":
    # 建立範例樹：1
    #           / \
    #          2   3
    #             / \
    #            4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    codec = Codec()
    s = codec.serialize(root)  # 序列化
    print("序列化結果：", s)  # 印出序列化字串
    t = codec.deserialize(s)  # 反序列化
    print("反序列化後根節點值：", t.val)  # 驗證還原結果
```

### BFS 實作
```python
from collections import deque  # 匯入 deque 作為佇列

class CodecBFS:
    def serialize(self, root):
        """
        層序遍歷序列化
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''  # 空樹
        queue = deque([root])  # 初始化佇列
        res = []  # 儲存序列化結果
        while queue:
            node = queue.popleft()  # 取出佇列左端節點
            if node:
                res.append(str(node.val))  # 加入節點值
                queue.append(node.left)  # 加入左子樹
                queue.append(node.right)  # 加入右子樹
            else:
                res.append('#')  # 空節點
        return ','.join(res)  # 以逗號串接

    def deserialize(self, data):
        """
        層序遍歷反序列化
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None  # 空樹
        vals = data.split(',')  # 拆分字串
        root = TreeNode(int(vals[0]))  # 建立根節點
        queue = deque([root])  # 初始化佇列
        i = 1  # 指向下一個值
        while queue:
            node = queue.popleft()  # 取出佇列左端節點
            if vals[i] != '#':
                node.left = TreeNode(int(vals[i]))  # 建立左子節點
                queue.append(node.left)  # 加入佇列
            i += 1
            if vals[i] != '#':
                node.right = TreeNode(int(vals[i]))  # 建立右子節點
                queue.append(node.right)  # 加入佇列
            i += 1
        return root
```

---
