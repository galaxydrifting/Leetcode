from typing import List


def maxProfit(prices: List[int]) -> int:
    max_profit = 0  # 最大利潤初始為 0
    left = 0        # left 指標，代表買入日
    # 遍歷每一天，right 指標代表賣出日
    for right in range(1, len(prices)):
        if prices[right] > prices[left]:  # 若賣出價高於買入價
            profit = prices[right] - prices[left]  # 計算利潤
            max_profit = max(max_profit, profit)   # 更新最大利潤
        else:
            left = right  # 若遇到更低價，更新買入日
    return max_profit  # 回傳最大利潤


if __name__ == "__main__":
    # 範例測試
    print(maxProfit([7, 1, 5, 3, 6, 4]))  # 輸出 5
    print(maxProfit([7, 6, 4, 3, 1]))    # 輸出 0
