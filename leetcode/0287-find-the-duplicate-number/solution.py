# 287. Find the Duplicate Number
# 題目要求：找出陣列中唯一重複的數字，不能修改原陣列且只能用常數空間
from typing import List

def findDuplicate(nums: List[int]) -> int:
    # 初始化快慢指針，皆指向陣列第一個元素
    slow = nums[0]  # 慢指針
    fast = nums[0]  # 快指針
    # 第一階段：快慢指針相遇
    while True:
        slow = nums[slow]        # 慢指針走一步
        fast = nums[nums[fast]] # 快指針走兩步
        if slow == fast:        # 相遇則跳出
            break
    # 第二階段：尋找循環入口
    slow = nums[0]              # 慢指針回到起點
    while slow != fast:
        slow = nums[slow]       # 慢指針走一步
        fast = nums[fast]       # 快指針走一步
    return slow                 # 相遇點即為重複數字

if __name__ == "__main__":
    # 範例測試
    test_cases = [
        [1, 3, 4, 2, 2],   # 預期輸出：2
        [3, 1, 3, 4, 2],   # 預期輸出：3
        [1, 1],            # 預期輸出：1
        [1, 1, 2],         # 預期輸出：1
    ]
    for nums in test_cases:
        print(f"輸入: {nums} -> 重複數字: {findDuplicate(nums)}")
