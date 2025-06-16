from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    # 將 nums1, nums2 指派給 A, B
    A, B = nums1, nums2  # A, B 分別指向兩個輸入陣列
    # 計算兩陣列總長度
    total = len(A) + len(B)  # 兩陣列總長度
    # 計算左半部元素個數
    half = total // 2  # 左半部元素個數
    # 若 B 較短則交換，確保 A 為較短陣列
    if len(B) < len(A):  # 若 B 較短則交換
        A, B = B, A
    # 設定二分搜尋範圍
    l, r = 0, len(A) - 1  # l, r 為 A 的搜尋範圍
    while True:
        # A 的分割點
        i = (l + r) // 2  # A 的分割點
        # B 的分割點，確保左半部元素數量正確
        j = half - i - 2  # B 的分割點

        # 取得分割點左右的值，若越界則用無窮大/小處理
        Aleft = A[i] if i >= 0 else float('-inf')  # A 左半最大值
        Aright = A[i + 1] if (i + 1) < len(A) else float('inf')  # A 右半最小值
        Bleft = B[j] if j >= 0 else float('-inf')  # B 左半最大值
        Bright = B[j + 1] if (j + 1) < len(B) else float('inf')  # B 右半最小值

        # 檢查分割是否正確
        if Aleft <= Bright and Bleft <= Aright:  # 分割正確
            if total % 2:  # 若總長度為奇數
                return min(Aright, Bright)  # 回傳右半最小值
            # 否則回傳左半最大值與右半最小值平均
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:  # Aleft 太大，i 太大
            r = i - 1  # 往左縮小範圍
        else:  # Aleft 太小，i 太小
            l = i + 1  # 往右擴大範圍


if __name__ == "__main__":
    # 範例測試
    nums1 = [1, 3]  # 測試資料1
    nums2 = [2]     # 測試資料2
    print(findMedianSortedArrays(nums1, nums2))  # 預期輸出：2.0
    nums1 = [1, 2]  # 測試資料3
    nums2 = [3, 4]  # 測試資料4
    print(findMedianSortedArrays(nums1, nums2))  # 預期輸出：2.5
