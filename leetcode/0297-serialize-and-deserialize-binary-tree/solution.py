from collections import deque  # 匯入 deque 作為佇列

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
                res.append('N')  # 空節點以 N 表示
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
            if vals[i] != 'N':
                node.left = TreeNode(int(vals[i]))  # 建立左子節點
                queue.append(node.left)  # 加入佇列
            i += 1
            if vals[i] != 'N':
                node.right = TreeNode(int(vals[i]))  # 建立右子節點
                queue.append(node.right)  # 加入佇列
            i += 1
        return root


# 範例測試
if __name__ == "__main__":
    # 建立範例樹：1
    #           / \
    #          2   3
    #             / \
    #            4   5
    root = TreeNode(1)  # 建立根節點 1
    root.left = TreeNode(2)  # 左子節點 2
    root.right = TreeNode(3)  # 右子節點 3
    root.right.left = TreeNode(4)  # 右子節點的左子節點 4
    root.right.right = TreeNode(5)  # 右子節點的右子節點 5

    codec = Codec()  # 建立 Codec 物件
    s = codec.serialize(root)  # 序列化
    print("序列化結果：", s)  # 印出序列化字串
    t = codec.deserialize(s)  # 反序列化
    print("反序列化後根節點值：", t.val)  # 驗證還原結果

    codec_bfs = CodecBFS()  # 建立 BFS Codec 物件
    s_bfs = codec_bfs.serialize(root)  # BFS 序列化
    print("BFS 序列化結果：", s_bfs)  # 印出 BFS 序列化字串
    t_bfs = codec_bfs.deserialize(s_bfs)  # BFS 反序列化
    print("BFS 反序列化後根節點值：", t_bfs.val)  # 驗證還原結果
