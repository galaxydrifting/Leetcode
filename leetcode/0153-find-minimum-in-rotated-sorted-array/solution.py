# 使用二分搜尋法尋找旋轉排序陣列中的最小值
class Solution:
    def findMin(self, nums):
        left = 0  # 左指標，指向陣列開頭
        right = len(nums) - 1  # 右指標，指向陣列結尾
        while left < right:  # 當左右指標未重疊時持續搜尋
            mid = (left + right) // 2  # 取中間索引
            if nums[mid] < nums[right]:  # 若中間值小於右端值
                right = mid  # 最小值在左半邊（包含 mid）
            else:  # 否則最小值在右半邊
                left = mid + 1  # 移動左指標到 mid 右側
        return nums[left]  # 返回最小值


if __name__ == "__main__":
    # 範例輸入
    nums = [4, 5, 6, 7, 0, 1, 2]
    sol = Solution()
    result = sol.findMin(nums)
    print(f"旋轉排序陣列 {nums} 的最小值為: {result}")
