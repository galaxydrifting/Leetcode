# 使用單調堆疊求解最大矩形面積
class Solution:
    def largestRectangleArea(self, heights):
        heights.append(0)  # 在 heights 後補 0，確保所有柱子都能被計算
        stack = []  # 初始化堆疊，存放柱子的索引
        max_area = 0  # 最大面積初始為 0
        for i, h in enumerate(heights):  # 遍歷每個柱子
            # 當堆疊不為空且當前高度小於堆疊頂端高度時
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]  # 取出堆疊頂端的高度
                # 如果堆疊為空，寬度就是 i，否則是 i - stack[-1] - 1
                width = i if not stack else i - stack[-1] - 1
                area = height * width  # 計算面積
                max_area = max(max_area, area)  # 更新最大面積
            stack.append(i)  # 將當前索引加入堆疊
        return max_area  # 回傳最大面積
