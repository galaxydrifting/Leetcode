# 二分搜尋法於 2D 矩陣
class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)  # 取得矩陣的列數
        n = len(matrix[0]) if m > 0 else 0  # 取得矩陣的行數
        left = 0  # 一維陣列的起始索引
        right = m * n - 1  # 一維陣列的結束索引
        while left <= right:  # 當搜尋區間有效時
            mid = (left + right) // 2  # 取中間索引
            row, col = divmod(mid, n)  # 同時計算列與行，使用 divmod 使程式更簡潔
            val = matrix[row][col]  # 取得對應元素
            if val == target:  # 若找到目標
                return True  # 回傳 True
            elif val < target:  # 若中間值小於目標
                left = mid + 1  # 移動左界
            else:  # 若中間值大於目標
                right = mid - 1  # 移動右界
        return False  # 未找到目標，回傳 False
