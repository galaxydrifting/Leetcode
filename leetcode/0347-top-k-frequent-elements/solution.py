from collections import Counter
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    # 直接用 Counter.most_common(k) 取得前 k 頻率元素
    return [item for item, _ in count.most_common(k)]


# 範例測試
if __name__ == "__main__":
    print(topKFrequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
    print(topKFrequent([1], 1))            # [1]
