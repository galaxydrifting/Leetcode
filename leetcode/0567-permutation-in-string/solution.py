from collections import Counter  # 匯入 Counter 用於字元計數


def checkInclusion(s1: str, s2: str) -> bool:
    s1_len = len(s1)  # 取得 s1 長度
    s2_len = len(s2)  # 取得 s2 長度
    if s1_len > s2_len:
        return False  # 若 s1 較長，直接回傳 False

    s1_count = Counter(s1)  # 計算 s1 各字元出現次數
    window = Counter(s2[:s1_len])  # 初始化視窗，計算前 s1_len 個字元

    if window == s1_count:
        return True  # 若初始視窗即符合，回傳 True

    for i in range(s1_len, s2_len):  # 從 s1_len 開始滑動視窗
        window[s2[i]] += 1  # 新增右側字元
        window[s2[i - s1_len]] -= 1  # 移除左側字元
        if window[s2[i - s1_len]] == 0:
            del window[s2[i - s1_len]]  # 若計數為 0，移除該字元
        if window == s1_count:
            return True  # 若視窗計數符合，回傳 True
    return False  # 遍歷完都沒找到，回傳 False


if __name__ == "__main__":
    # 範例測試
    print(checkInclusion("ab", "eidbaooo"))  # True
    print(checkInclusion("ab", "eidboaoo"))  # False
