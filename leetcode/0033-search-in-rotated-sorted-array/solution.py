# 搜尋旋轉排序陣列
from typing import List

def search(nums: List[int], target: int) -> int:
    left = 0  # 左指標
    right = len(nums) - 1  # 右指標
    while left <= right:  # 當左指標不超過右指標時
        mid = (left + right) // 2  # 取中間索引
        if nums[mid] == target:  # 若找到目標
            return mid  # 回傳索引
        # 判斷哪一半是有序的
        if nums[left] <= nums[mid]:  # 左半邊有序
            if nums[left] <= target < nums[mid]:  # 目標在左半邊
                right = mid - 1  # 縮小右邊界
            else:
                left = mid + 1  # 否則搜尋右半邊
        else:  # 右半邊有序
            if nums[mid] < target <= nums[right]:  # 目標在右半邊
                left = mid + 1  # 縮小左邊界
            else:
                right = mid - 1  # 否則搜尋左半邊
    return -1  # 未找到目標

if __name__ == "__main__":
    # 範例測試
    nums1 = [4,5,6,7,0,1,2]
    print(search(nums1, 0))  # 輸出: 4
    print(search(nums1, 3))  # 輸出: -1
    nums2 = [1]
    print(search(nums2, 0))  # 輸出: -1
