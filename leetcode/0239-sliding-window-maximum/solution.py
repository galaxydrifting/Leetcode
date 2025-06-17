from collections import deque  # 匯入雙端佇列
from typing import List        # 匯入型別註解


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    res = []  # 儲存每個視窗的最大值
    q = deque()  # 儲存索引，維持單調遞減
    for i, n in enumerate(nums):  # 遍歷每個元素與其索引
        while q and nums[q[-1]] < n:  # 移除隊尾小於當前元素的索引
            q.pop()  # 移除隊尾
        q.append(i)  # 將當前索引加入隊尾
        if q[0] <= i - k:  # 移除已滑出視窗的隊首索引
            q.popleft()
        if i >= k - 1:  # 當視窗長度達到 k 時，將最大值加入結果
            res.append(nums[q[0]])
    return res


if __name__ == "__main__":
    # 範例測試
    nums = [1, 3, -1, -3, 5, 3, 6, 7]  # 測試資料
    k = 3  # 視窗大小
    print(maxSlidingWindow(nums, k))  # 輸出: [3,3,5,5,6,7]
    nums2 = [1]
    k2 = 1
    print(maxSlidingWindow(nums2, k2))  # 輸出: [1]
