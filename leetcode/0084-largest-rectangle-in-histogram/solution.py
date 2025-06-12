from typing import List


def largestRectangleArea(heights: List[int]) -> int:
    stack = []  # 儲存索引
    max_area = 0
    heights.append(0)  # 在最後加一個 0，確保所有柱子都會被處理
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    heights.pop()  # 還原 heights
    return max_area
