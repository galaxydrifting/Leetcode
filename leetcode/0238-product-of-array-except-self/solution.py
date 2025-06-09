from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    answer = [1] * n
    left = 1
    for i in range(n):
        answer[i] = left
        left *= nums[i]
    right = 1
    for i in range(n-1, -1, -1):
        answer[i] *= right
        right *= nums[i]
    return answer

# --- 補充：分別計算左右乘積再相乘的寫法 ---
# def productExceptSelf(nums: List[int]) -> List[int]:
#     n = len(nums)
#     left_products = [1] * n
#     right_products = [1] * n
#     # 計算左乘積
#     for i in range(1, n):
#         left_products[i] = left_products[i-1] * nums[i-1]
#     # 計算右乘積
#     for i in range(n-2, -1, -1):
#         right_products[i] = right_products[i+1] * nums[i+1]
#     # 左右乘積相乘
#     answer = [left_products[i] * right_products[i] for i in range(n)]
#     return answer


if __name__ == "__main__":
    # 測試範例
    print(productExceptSelf([1, 2, 3, 4]))      # [24, 12, 8, 6]
    print(productExceptSelf([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]
