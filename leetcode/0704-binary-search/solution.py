# 二分搜尋法實作
# nums: 已排序的整數陣列
# target: 要搜尋的目標值
# 回傳 target 的索引，若不存在則回傳 -1

def search(nums, target):
    left = 0  # 左指標，起始為 0
    right = len(nums) - 1  # 右指標，起始為陣列最後一個索引
    while left <= right:  # 當左指標不超過右指標時持續搜尋
        mid = (left + right) // 2  # 取中間索引
        if nums[mid] == target:  # 若中間值等於目標值
            return mid  # 回傳索引
        elif nums[mid] < target:  # 若中間值小於目標值
            left = mid + 1  # 移動左指標到 mid 右邊
        else:  # 若中間值大於目標值
            right = mid - 1  # 移動右指標到 mid 左邊
    return -1  # 若未找到目標值，回傳 -1
