# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # 節點值
        self.left = left  # 左子樹
        self.right = right  # 右子樹


class Solution:
    def buildTree(self, preorder, inorder):
        # 建立中序值到索引的映射，加速查找
        inorder_index = {val: idx for idx, val in enumerate(inorder)}  # 哈希表

        def helper(pre_left, pre_right, in_left, in_right):
            # 若沒有元素，返回 None
            if pre_left > pre_right:
                return None
            # 前序的第一個元素是根節點
            root_val = preorder[pre_left]
            root = TreeNode(root_val)  # 建立根節點
            # 根節點在中序的位置
            in_root_idx = inorder_index[root_val]
            # 左子樹節點數量
            left_size = in_root_idx - in_left
            # 遞迴構建左子樹
            root.left = helper(pre_left+1, pre_left +
                               left_size, in_left, in_root_idx-1)
            # 遞迴構建右子樹
            root.right = helper(pre_left+left_size+1,
                                pre_right, in_root_idx+1, in_right)
            return root  # 返回根節點

        # 從整個區間開始遞迴
        return helper(0, len(preorder)-1, 0, len(inorder)-1)


# 範例測試
if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]  # 前序遍歷
    inorder = [9, 3, 15, 20, 7]   # 中序遍歷
    sol = Solution()
    root = sol.buildTree(preorder, inorder)  # 構建樹

    # 輔助函式：層序遍歷輸出樹結構
    from collections import deque

    def print_tree(root):
        if not root:
            print([])
            return
        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        # 去除尾部多餘的 None
        while result and result[-1] is None:
            result.pop()
        print(result)
    print_tree(root)  # 輸出: [3, 9, 20, None, None, 15, 7]
