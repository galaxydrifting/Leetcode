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
