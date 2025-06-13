from typing import List


def minEatingSpeed(piles: List[int], h: int) -> int:
    left = 1  # 最小速度設為1
    right = max(piles)  # 最大速度設為最大堆香蕉數
    while left < right:  # 當左界小於右界時持續搜尋
        mid = (left + right) // 2  # 取中間速度
        hours = 0  # 初始化總小時數
        for pile in piles:  # 遍歷每一堆香蕉
            hours += (pile + mid - 1) // mid  # 計算吃完該堆所需小時數，向上取整
        if hours <= h:  # 如果總小時數小於等於h
            right = mid  # 嘗試更慢的速度
        else:
            left = mid + 1  # 需要更快的速度
    return left  # 返回最小可行速度
