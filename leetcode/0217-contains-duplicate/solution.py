def containsDuplicate(nums):
    return len(nums) != len(set(nums))

# 進階寫法：遇到重複即提前回傳
# def containsDuplicate(nums):
#     seen = set()
#     for num in nums:
#         if num in seen:
#             return True
#         seen.add(num)
#     return False


if __name__ == "__main__":
    # 範例測試資料
    nums1 = [1, 2, 3, 1]  # 有重複，應回傳 True
    nums2 = [1, 2, 3, 4]  # 無重複，應回傳 False
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]  # 有重複，應回傳 True

    print(f"測試 1: {containsDuplicate(nums1)}")  # 預期 True
    print(f"測試 2: {containsDuplicate(nums2)}")  # 預期 False
    print(f"測試 3: {containsDuplicate(nums3)}")  # 預期 True
