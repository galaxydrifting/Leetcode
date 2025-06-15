from collections import defaultdict
# import bisect  # 面試時建議不用，可作為補充


class TimeMap:
    def __init__(self):
        # 用 dict 儲存每個 key 的 (timestamp, value) 列表
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))  # 直接 append，timestamp 遞增

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""  # 若 key 不存在，回傳空字串
        arr = self.store[key]
        # 手動二分搜尋，找最大且 <= timestamp 的 timestamp
        left, right = 0, len(arr) - 1
        res = ""
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]  # 更新答案，繼續往右找
                left = mid + 1
            else:
                right = mid - 1
        return res
        # --- 補充：若允許使用 bisect 模組，可用下列寫法 ---
        # i = bisect.bisect_right(arr, (timestamp, chr(127)))
        # if i == 0:
        #     return ""
        # return arr[i-1][1]


if __name__ == "__main__":
    kv = TimeMap()
    kv.set("foo", "bar", 1)
    print(kv.get("foo", 1))   # 輸出 "bar"
    print(kv.get("foo", 3))   # 輸出 "bar"
    kv.set("foo", "bar2", 4)
    print(kv.get("foo", 4))   # 輸出 "bar2"
    print(kv.get("foo", 5))   # 輸出 "bar2"
